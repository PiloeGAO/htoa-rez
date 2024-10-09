name = "htoa"

version = "6.3.4.1"

authors = [
    "Autodesk"
]

requires = [
    "houdini-20.5.332",
]

description = \
    """
    Arnold for Houdini.
    """

uuid = "autodesk.htoa"

build_command = "python {root}/build.py {install}"

def commands():
    if "\\\\svm-users\\dev" in root:
        root = root.replace("\\\\svm-users\\dev", "Z:")

    env.HOUDINI_PACKAGE_DIR.prepend("{root}/houdini/packages") 
