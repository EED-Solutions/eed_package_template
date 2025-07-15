from pathlib import Path
import importlib


def test_package_import():
    # Get the git root folder name
    current_file = Path(__file__)
    git_root = next(iter(current_file.parents))
    while not (git_root / ".git").exists() and git_root != git_root.parent:
        git_root = git_root.parent
    package_name = git_root.name

    # Import the package with the same name as the git root folder
    package = importlib.import_module(package_name)

    print(package.__path__)
    assert True
