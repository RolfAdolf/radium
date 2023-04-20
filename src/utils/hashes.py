from aiofile import async_open

import asyncio
import os
import hashlib
from typing import Union, Dict
from pathlib import Path

from src.utils import dirs, prints


directory: os.PathLike = Path('/')
hashes: Dict[str, str] = {}


async def calc_hash_for_file(filename: Union[str, os.PathLike]):
    global hashes
    file_path = directory / filename
    print(f'Reading {filename} file...')
    try:
        async with async_open(file_path, 'rb') as file:
            bts = await file.read()
            print(f'Calculating hash for {filename}...')
            hsh = hashlib.sha256(bts).hexdigest()
            hashes[filename] = hsh
    except FileNotFoundError:
        hashes[filename] = f"File {filename} doesn't exist in {directory}"


@prints.async_bounds_printer(
    'Calculating sha_256 for every file',
    'Hashes have been calculated',
)
async def sha_256_calculate(
        directory_: Union[str, os.PathLike]
) -> Dict[str, str]:

    global directory
    directory = Path(directory_)
    files = dirs.all_files(directory)

    readers = [calc_hash_for_file(file) for file in files]

    await asyncio.gather(*readers)

    print_hashes()


def print_hashes() -> None:
    global hashes
    print('\n', 10 * '-', 'CALCULATED HASHES', 10 * '-')
    output = [f'{key}: {value}' for key, value in hashes.items()]
    output = '\n'.join(output)
    print(output)
