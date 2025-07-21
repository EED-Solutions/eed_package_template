from eed_basic_utils.os import get_git_root


def hello_world() -> str:
    """
    Returns a greeting message.

    This function is part of the eed-package-template and can be used to verify that the package is set up correctly.
    """
    git_root = get_git_root()
    return f"Hello from {git_root}!"
