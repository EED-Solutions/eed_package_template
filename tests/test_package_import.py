import importlib


def test_package_import(cfg_test):
    """Test importing a package with the same name as the git root folder."""
    package_name = cfg_test["git_root"].name
    # Import the package with the same name as the git root folder
    package = importlib.import_module(package_name)

    print(package.__path__)
    assert True
