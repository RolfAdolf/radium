import os
import io
from pathlib import Path
import sys

from src.utils import dirs


def test_make_dir(prepare_test_directory):

    directory = Path(prepare_test_directory)

    # Test creating directory
    test_dir = directory / 'make_temp_dir'
    dirs.make_temp_dir(test_dir)
    assert test_dir.is_dir()
    assert os.listdir(test_dir) == []

    # Test directory, which already exists
    dirs.make_temp_dir(directory)
    assert os.listdir(directory) == []


def test_print_files(prepare_test_directory):

    output_stream = io.StringIO()
    sys.stdout = output_stream
    dirs.print_files(prepare_test_directory)

    # Check if output is empty
    assert output_stream.getvalue()

    fake_files = 'fake_test_directory_fake'

    output_stream = io.StringIO()
    sys.stdout = output_stream
    dirs.print_files(fake_files)

    assert 'No such file or directory' in output_stream.getvalue()

    sys.stdout = sys.__stdout__


def test_all_files(prepare_test_directory):
    result = dirs.all_files(prepare_test_directory)
    expected = [
        'test_dir/test_file_0',
        'test_dir/test_file_1',
        'test_dir/test_file_2',
        'test_file_0',
        'test_file_1',
        'test_file_2',
    ]
    assert set(result) == set(expected)

    fake_files = 'fake_test_directory_fake'

    output_stream = io.StringIO()
    sys.stdout = output_stream
    dirs.all_files(fake_files)

    assert "Can't find the" in output_stream.getvalue()

    sys.stdout = sys.__stdout__
