"""Lock dependencies when uv is already installed."""

import shutil
import subprocess
import sys


def main():
    if shutil.which("uv") is None:
        print("uv was not found. Install uv, then run `uv lock` in the new project.")
        return
    subprocess.run(["uv", "lock"], check=True)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        sys.exit(exc.returncode)
