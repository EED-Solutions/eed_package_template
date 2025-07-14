def test_package_import():
    import edd_package_template

    print(edd_package_template.__path__)
    assert True
