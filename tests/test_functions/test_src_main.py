import os
import asyncio
from pathlib import Path

from src import main


def test_write_file(prepare_test_directory):

    directory = Path(prepare_test_directory)
    test_file = 'test_file.txt'

    main.folder_name = directory

    asyncio.run(main.write_file(test_file, '123'))

    with open(directory / test_file) as file:
        result = file.read()

    assert result == '123'


def test_main(prepare_test_directory):

    result = os.system('python3 -m src.main')

    assert result == 0
