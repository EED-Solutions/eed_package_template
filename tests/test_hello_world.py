from eed_package_template import hello_world


def test_hello_world() -> None:
    """
    Test the hello_world function.

    This test verifies that the hello_world function returns a greeting message
    that includes the git root directory.
    """
    result = hello_world()
    assert "Hello from" in result, "Greeting message should start with 'Hello from'"
    assert "eed_package_template" in result, "Greeting message should include 'eed-package-template'"
