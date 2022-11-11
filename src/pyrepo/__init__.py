"""package description."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyrepo")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Talley Lambert"
__email__ = "talley.lambert@gmail.com"


def do_a_thing() -> bool:
    """Do a thing."""
    print("Doing a thing!")
    return True
