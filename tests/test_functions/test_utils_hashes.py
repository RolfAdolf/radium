import asyncio
import hashlib
from pathlib import Path
import io
import sys

from src.utils import hashes


def test_calc_hash_for_file(prepare_test_directory):

    directory = Path(prepare_test_directory)
    hashes.directory = directory
    file_path = directory / 'test_file_0'

    with open(file_path, 'rb') as file:
        content = file.read()
        expected = hashlib.sha256(content).hexdigest()
        asyncio.run(hashes.calc_hash_for_file('test_file_0'))
        result = hashes.hashes['test_file_0']
        assert expected == result

    fake_file = 'non_exist_file'
    asyncio.run(hashes.calc_hash_for_file(fake_file))
    expected = f"File {fake_file} doesn't exist in {hashes.directory}"
    assert expected == hashes.hashes[fake_file]


def test_sha_256_calculate(prepare_test_directory):
    directory = Path(prepare_test_directory)
    hashes.directory = directory

    asyncio.run(hashes.sha_256_calculate(directory))

    expected = [
        'test_dir/test_file_0',
        'test_dir/test_file_1',
        'test_dir/test_file_2',
        'test_file_0',
        'test_file_1',
        'test_file_2',
    ]

    for filename in expected:
        assert filename in hashes.hashes


def test_print_hashes():
    hashes.hashes = {
        'test_1': '123test'
    }

    output_stream = io.StringIO()
    sys.stdout = output_stream
    hashes.print_hashes()
    sys.stdout = sys.__stdout__

    # Check if output is empty
    assert '123test' in output_stream.getvalue()
