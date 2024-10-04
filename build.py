import os
import os.path
import shutil
import sys


def build(source_path, build_path, install_path, targets):

    folder = "houdini"

    def _build():
        src = os.path.join(source_path, folder)
        dest = os.path.join(build_path, folder)

        if not os.path.exists(dest):
            shutil.copytree(src, dest)

    def _install():
        src = os.path.join(build_path, folder)
        dest = os.path.join(install_path, folder)

        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(src, dest)

    _build()

    if "install" in (targets or []):
        _install()


if __name__ == "__main__":
    build(
        source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
        build_path=os.environ["REZ_BUILD_PATH"],
        install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
        targets=sys.argv[1:],
    )
