from collections.abc import Iterator

import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def cfg_test() -> Iterator[dict]:
    home_dir = str(Path.home())
    cfg_test = {
        "home_dir": home_dir,
    }
    yield cfg_test
