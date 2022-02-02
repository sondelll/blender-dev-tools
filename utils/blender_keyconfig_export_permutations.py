# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>


"""
This script exports permutations of key-maps with different settings modified.

Useful for checking changes intended for one configuration don't impact others accidentally.

./blender.bin \
    -b --factory-startup \
    --python source/tools/utils/blender_keyconfig_export_permutations.py -- \
    --output-dir=./output \
    --keymap-prefs=select_mouse:rmb_action

The preferences setting: ``select_mouse:rmb_action`` expands into:

config = [
    ("select_mouse", ('LEFT', 'RIGHT')),
    ("rmb_action", ('TWEAK', 'FALLBACK_TOOL')),
]
"""

import os
import sys

import bpy
from bpy import context


def argparse_create():
    import argparse

    parser = argparse.ArgumentParser(
        description="Parse keymap combination arguments",
    )

    parser.add_argument(
        "--output-dir",
        dest="output_dir",
        default=".",
        metavar='OUTPUT_DIR', type=str,
        help="The directory to output to.",
        required=False,
    )

    parser.add_argument(
        "--keymap-prefs",
        dest="keymap_prefs",
        default="select_mouse:rmb_action",
        metavar='KEYMAP_PREFS', type=str,
        help=(
            "Colon separated list of attributes to generate key-map configuration permutations. "
            "WARNING: as all combinations are tested, their number increases exponentially!"
        ),
        required=False,
    )

    return parser


def permutations_from_attrs_impl(config, permutation, index):
    index_next = index + 1
    attr, values = config[index]
    for val in values:
        permutation[index] = (attr, val)
        if index_next == len(config):
            yield tuple(permutation)
        else:
            # Keep walking down the list of permutations.
            yield from permutations_from_attrs_impl(config, permutation, index_next)
    # Not necessary, just ensure stale values aren't used.
    permutation[index] = None


def permutations_from_attrs(config):
    """
    Take a list of attributes and possible values:

        config = [
            ("select_mouse", ('LEFT', 'RIGHT')),
            ("rmb_action", ('TWEAK', 'FALLBACK_TOOL')),
        ]

    Yielding all permutations:

        [("select_mouse", 'LEFT'), ("rmb_action", 'TWEAK')],
        [("select_mouse", 'LEFT'), ("rmb_action", 'FALLBACK_TOOL')],
        ... etc ...
    """
    permutation = [None] * len(config)
    result = list(permutations_from_attrs_impl(config, permutation, 0))
    assert permutation == ([None] * len(config))
    return result


def permutation_as_filename(values):
    """
    Takes a configuration, eg:

        [("select_mouse", 'LEFT'), ("rmb_action", 'TWEAK')]

    And returns a filename compatible path:
    """
    from urllib.parse import quote
    return quote(
        ".".join([
            "-".join((str(key), str(val)))
                for key, val in values
        ]),
        # Needed so forward slashes aren't included in the resulting name.
        safe="",
    )


def main():
    args = argparse_create().parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])

    output_dir = args.output_dir

    os.makedirs(output_dir, exist_ok=True)

    # Needed for background mode.
    preset_filepath = bpy.utils.preset_find("Blender", preset_path="keyconfig")
    bpy.ops.preferences.keyconfig_activate(filepath=preset_filepath)

    # Key-map preferences..
    km_prefs = context.window_manager.keyconfigs.active.preferences
    config = []
    # Use RNA introspection:
    for attr in args.keymap_prefs.split(":"):
        if not hasattr(km_prefs, attr):
            print(f"KeyMap preferences does not have attribute: {attr:s}")
            sys.exit(1)

        prop_def = km_prefs.rna_type.properties.get(attr)
        match prop_def.type:
            case 'ENUM':
                value = tuple(val.identifier for val in prop_def.enum_items)
            case 'BOOLEAN':
                value = (True, False)
            case _ as prop_def_type:
                raise Exception(f"Unhandled attribute type {prop_def_type:s}")
        config.append((attr, value))
    config = tuple(config)

    for attr_permutation in permutations_from_attrs(config):
        print(attr_permutation)

        # Reload and set.
        km_prefs = context.window_manager.keyconfigs.active.preferences
        for attr, value in attr_permutation:
            setattr(km_prefs, attr, value)
        # Re-activate after setting preferences, tsk, ideally this shouldn't be necessary.
        bpy.ops.preferences.keyconfig_activate(filepath=preset_filepath)

        filepath = os.path.join(output_dir, permutation_as_filename(attr_permutation) + ".py")

        print("Writing:", filepath)
        bpy.ops.preferences.keyconfig_export(filepath=filepath, all=True)

    sys.exit()


if __name__ == "__main__":
    main()
