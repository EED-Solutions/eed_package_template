def test_package_import():
    import eed_package_template

    print(eed_package_template.__path__)
    assert True
