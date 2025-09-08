name = "htoa"

version = "6.4.4.0"

authors = [
    "Autodesk"
]

requires = [
    "houdini-21.0.440",
]

description = \
    """
    Arnold for Houdini.
    """

uuid = "autodesk.htoa"

build_command = "python {root}/build.py {install}"

def commands():
    if "\\\\srv-sto-02\\dev" in root:
        root = root.replace("\\\\srv-sto-02\\dev", "Z:")

    env.HOUDINI_PACKAGE_DIR.prepend("{root}/houdini/packages") 
