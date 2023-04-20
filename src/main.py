from aiohttp import ClientSession
from aiofile import async_open

import os
import asyncio
from typing import Union
from pathlib import Path
import tempfile

from src.utils import dirs, links, hashes, prints


async def write_file(file_path: Union[str, os.PathLike], data: str) -> None:
    print(f'Writing {file_path}')
    async with async_open(folder_name / file_path, 'w+') as file:
        await file.write(data)


async def fetch(session: ClientSession, url: str) -> None:

    while links.files:
        file = links.files.pop(0)
        file_url = links.return_link(url, file)

        print(f'Requesting file {file}')

        async with session.get(file_url) as response:
            data = await response.read()
            await write_file(file, data.decode())


@prints.async_bounds_printer(
    'Start downloading files',
    'Files has been downloaded successfully'
)
async def main():
    async with ClientSession() as session:
        url = links.rep_url
        fetchers = [fetch(session, url) for _ in range(3)]
        await asyncio.gather(*fetchers)


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as output_folder:

        print(f'\nTemporary directory has been created at {output_folder}\n')

        folder_name = Path(output_folder) / 'project-configuration'
        sub_folder_name = folder_name / 'nitpick'
        for folder in (folder_name, sub_folder_name):
            dirs.make_temp_dir(folder)

        asyncio.run(main())

        dirs.print_files(folder_name)

        asyncio.run(hashes.sha_256_calculate(folder_name))

        directory = output_folder

    print(f'Temporary folder {directory} has been deleted.\n')
