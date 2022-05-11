# SPDX-License-Identifier: GPL-2.0-or-later

# <pep8 compliant>

# these must be all lower case for comparisons

dict_custom = {
    # Added to newer versions of the dictionary,
    # we can remove these when the updated word-lists have been applied to aspell-en.
    "accessor",
    "accessors",
    "completer",
    "completers",
    "enqueue",
    "enqueued",
    "enqueues",
    "intrinsics",
    "iterable",
    "parallelization",
    "parallelized",
    "pipelining",
    "polygonization",
    "prepend",
    "prepends",
    "rasterize",
    "reachability",
    "runtime",
    "runtimes",
    "serializable",
    "unary",
    "variadic",

    # Correct spelling, update the dictionary, here:
    # https://github.com/en-wl/wordlist
    "accessor",
    "additively",
    "adjoint",
    "adjugate",
    "affectable",
    "alignable",
    "allocatable",
    "allocator",
    "allocators",
    "anisotropic",
    "anisotropy",
    "atomicity",
    "boolean",
    "borderless",
    "breaked",
    "callables",
    "canonicalization",
    "canonicalized",
    "canonicalizing",
    "catadioptric",
    "checksums",
    "clearcoat",
    "collinear",
    "comparator",
    "comparators",
    "compilable",
    "confusticate",
    "confusticated",
    "constructability",
    "coplanarity",
    "copyable",
    "counterforce",
    "criterium",
    "crosstalk",
    "customizable",
    "deallocate",
    "deallocated",
    "deallocating",
    "decorrelated",
    "decrement",
    "decrementing",
    "deduplicating",
    "deduplication",
    "degeneracies",
    "deleter",
    "denoised",
    "denoiser",
    "denoising",
    "dereference",
    "dereferenced",
    "dereferencing",
    "desaturate",
    "designator",
    "destructor",
    "destructors",
    "dialogs",
    "dihedral",
    "discoverability",
    "discretization",
    "discretized",
    "discretizes",
    "downcasting",
    "durations",
    "eachother",
    "editability",
    "effector",
    "effectors",
    "embedder",
    "enablement",
    "enqueueing",
    "equiangular",
    "extrema",
    "finalizer",
    "flushable",
    "formatter",
    "formatters",
    "glitchy",
    "haptics",
    "highlightable",
    "homogenous",
    "ideographic",
    "illuminant",
    "incrementation",
    "initializer",
    "initializers",
    "instancer",
    "instancers",
    "instantiable",
    "instantiation",
    "instantiations",
    "interferences",
    "interocular",
    "invariants",
    "invisibilities",
    "irradiance",
    "iteratively",
    "jitteryness",
    "linkable",
    "luminances",
    "mappable",
    "merchantability",
    "mergeable",
    "minimalistic",
    "misconfiguration",
    "misconfigured",
    "monoscopy",
    "monospaced",
    "mutators",
    "natively",
    "occludee",
    "occluder",
    "occluders",
    "optionals",
    "orthogonalize",
    "orthonormalize",
    "orthonormalized",
    "overridable",
    "paddings",
    "pannable",
    "parallelize",
    "parallelizing",
    "parameterization",
    "parametrization",
    "parentless",
    "passepartout",
    "passthrough",
    "performant",
    "pixelate",
    "pixelated",
    "pixelisation",
    "planarity",
    "polygonizer",
    "polytope",
    "postprocess",
    "postprocessed",
    "pre-filtered",
    "pre-multiplied",
    "precalculate",
    "precisions",
    "precomputations",
    "precompute",
    "precomputed",
    "precomputing",
    "prefetch",
    "prefetching",
    "prefilter",
    "prefiltered",
    "prefiltering",
    "premutliplied",
    "prepend",
    "prepending",
    "preprocess",
    "preprocessing",
    "preprocessor",
    "preprocessors",
    "preventively",
    "probabilistically",
    "procedurally",
    "profiler",
    "quadratically",
    "rasterizer",
    "rasterizes",
    "rasterizing",
    "reallocations",
    "rebalancing",
    "recomputation",
    "recurse",
    "recursed",
    "recurses",
    "recursing",
    "recursivity",
    "redistributions",
    "registerable",
    "remappable",
    "remapper",
    "remappings",
    "remesher",
    "rendeder",
    "renderable",
    "renormalize",
    "renormalized",
    "reparameterization",
    "reparametization",
    "repurpose",
    "retiming",
    "reusability",
    "saveable",
    "schemas",
    "serializers",
    "sharpnesses",
    "sidedness",
    "skippable",
    "sortable",
    "stitchable",
    "subclass",
    "subclasses",
    "subclassing",
    "subdirectories",
    "subdirectory",
    "templating",
    "tertiarily",
    "tokenize",
    "tokenizing",
    "transmissive",
    "triangulations",
    "triangulator",
    "trilinear",
    "tunable",
    "unassign",
    "unbuffered",
    "unclamped",
    "uncollapsed",
    "uncomment",
    "uncommented",
    "unconfigured",
    "undisplaced",
    "uneditable",
    "unflagged",
    "unfoldable",
    "unformatted",
    "unhandled",
    "unkeyframed",
    "unlink",
    "unlinkable",
    "unlinked",
    "unlinking",
    "unmaximized",
    "unnormalized",
    "unparameterized",
    "unparsed",
    "unpause",
    "unpaused"
    "unproject",
    "unquantifiable",
    "unregister",
    "unregisters",
    "unselected",
    "unsynchronized",
    "untag",
    "untagging",
    "untrusted",
    "unusably",
    "unvisited",
    "userless",
    "vectorial",
    "vectorization",
    "vectorized",
    "versionable",
    "videogrammetry",
    "virtualized",
    "visibilities",
    "volumetrics",
    "vortices",
    "voxelize",
    "writeable",
    "zoomable",

    # C/C++/Python types (we could quote every instance but it's impractical).
    "enum",
    "enums",
    "int",
    "ints",
    "nullptr",  # C++ NULL-pointer.
    "str",
    "tuple",
    "tuples",

    # python functions
    "func",
    "repr",

    # Accepted concatenations.
    "addon",
    "addons",
    "autocomplete",
    "colospace",
    "datablock",
    "datablocks",
    "keyframe",
    "keyframing",
    "lookup",
    "lookups",
    "multithreaded",
    "multithreading",
    "namespace",
    "reparent",
    "tooltip",
    "unparent",

    # Accepted abbreviations.
    "anim",  # animation.
    "config",  # configuration.
    "coord",
    "coords",
    # "dir",  # direction/directory.
    "iter",  # iteration.
    "multi",
    "numpad",  # numeric-pad.
    "numpads",  # numeric-pads.
    "ortho",
    "recalc",
    "resync",
    "struct",
    "structs",
    "subdir",

    # General computer terms.
    "app",
    "ascii",
    "autocomplete",
    "autorepeat",
    "blit",
    "blitting",
    "boids",
    "booleans",
    "codepage",
    "contructor",
    "decimator",
    "diff",
    "diffs",
    "endian",
    "endianness",
    "env",
    "euler",
    "eulers",
    "foo",
    "hashable",
    "http",
    "intelisense",
    "jitter",
    "jittering",
    "keymap",
    "lerp",
    "metadata",
    "mutex",
    "opengl",
    "quantized",
    "searchable",
    "segfault",
    "stdin",
    "stdin",
    "stdout",
    "sudo",
    "threadsafe",
    "touchpad",
    "touchpads",
    "trackpad",
    "trackpads",
    "unicode",
    "usr",
    "vert",
    "verts",
    "voxel",
    "voxels",
    "wiki",

    # specific computer terms/brands
    "ack",
    "amiga",
    "cmake",
    "ffmpeg",
    "freebsd",
    "linux",
    "manpage",
    "mozilla",
    "nvidia",
    "openexr"
    "posix",
    "qtcreator",
    "unix",
    "valgrind",
    "xinerama",

    # general computer graphics terms
    "atomics",
    "barycentric",
    "bezier",
    "bicubic",
    "bitangent",
    "centroid",
    "colinear",
    "compositing",
    "coplanar",
    "crypto",
    "deinterlace",
    "emissive",
    "fresnel",
    "gaussian",
    "kerning",
    "lacunarity",
    "lossless",
    "lossy",
    "luma",
    "mipmap",
    "mipmapped",
    "mipmapping",
    "mipmaps",
    "musgrave",
    "n-gon",
    "n-gons",
    "normals",
    "nurbs",
    "octree",
    "quaternions",
    "radiosity",
    "reflectance",
    "shader",
    "shaders",
    "specular",

    # Blender specific terms.
    "animsys",
    "animviz",
    "bmain",
    "bmesh",
    "bpy",
    "depsgraph",
    "doctree",
    "editmode",
    "eekadoodle",
    "fcurve",
    "look-dev",
    "mathutils",
    "obdata",
    "userpref",
    "userprefs",

    # Should have apostrophe but ignore for now unless we want to get really picky!
    "indices",
    "vertices",
}

# incorrect spelling but ignore anyway
dict_ignore = {
    "a-z",
    "animatable",
    "arg",
    "args",
    "bool",
    "constness",
    "dirpath",
    "dupli",
    "eg",
    "filename",
    "filenames",
    "filepath",
    "filepaths",
    "hardcoded",
    "id-block",
    "inlined",
    "loc",
    "namespace",
    "node-trees",
    "ok",
    "ok-ish",
    "param",
    "polyline",
    "polylines",
    "premultiplied",
    "premultiply",
    "pylint",
    "quad",
    "readonly",
    "submodule",
    "submodules",
    "tooltips",
    "tri",
    "ui",
    "unfuzzy",
    "utils",
    "uv",
    "vec",
    "wireframe",
    "x-axis",
    "y-axis",
    "z-axis",

    # acronyms
    "api",
    "cpu",
    "gl",
    "gpl",
    "gpu",
    "gzip",
    "hg",
    "ik",
    "lhs",
    "nan",
    "nla",
    "ppc",
    "rgb",
    "rhs",
    "rna",
    "smpte",
    "svn",
    "utf",

    # extensions
    "py",
    "rst",
    "xml",
    "xpm",

    # tags
    "fixme",
    "todo",

    # sphinx/rst
    "rtype",

    # slang
    "automagically",
    "hacky",
    "hrmf",

    # names
    "campbell",
    "jahka",
    "mikkelsen",
    "morten",

    # Company names.
    "Logitech",
    "Wacom",

    # Project Names.
    "Wayland",

    # clang-tidy (for convenience).
    "bugprone-suspicious-enum-usage",
    "bugprone-use-after-move",
}

# Allow: `un-word`, `re-word` ... etc, in this case only check `word`.
dict_ignore_hyphenated_prefix = {
    "de",
    "mis",
    "non",
    "post",
    "pre",
    "re",
    "un",
}

dict_ignore_hyphenated_suffix = {
    "ify",
    "ish",
    "ness",
}

files_ignore = {
    "source/tools/utils_doc/rna_manual_reference_updater.py",  # Contains language ID references.
}
