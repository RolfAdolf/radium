import pytest

import os
from pathlib import Path
import tempfile


@pytest.fixture()
def create_dir():
    with tempfile.TemporaryDirectory() as test_folder:
        yield test_folder


@pytest.fixture()
def prepare_test_directory(create_dir):

    directory = Path(create_dir)

    def fill_dir(directory_: os.PathLike) -> None:
        directory_ = Path(directory_)
        for i in range(3):
            filename = f'test_file_{i}'
            with open(directory_ / filename, 'w') as file:
                file.write(filename)

    fill_dir(directory)

    test_dir = directory / 'test_dir'
    os.mkdir(test_dir)
    fill_dir(test_dir)

    yield directory
