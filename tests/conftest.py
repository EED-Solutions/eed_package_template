from collections.abc import Iterator

import pytest
from pathlib import Path
from eed_basic_utils.os import get_git_root


@pytest.fixture(scope="session")
def cfg_test() -> Iterator[dict]:
    home_dir = Path.home()
    cfg_test = {
        "home_dir": home_dir,
        "cwd": Path.cwd(),
        "git_root": get_git_root(),
    }
    yield cfg_test
