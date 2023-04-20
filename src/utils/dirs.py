import os
import shutil
from typing import Union, List
from pathlib import Path

from src.utils import prints


def clear_dir(dir_name: Union[str, os.PathLike]) -> None:
    for file in os.listdir(dir_name):
        file_path = dir_name / file
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def make_temp_dir(
        dir_name: Union[str, os.PathLike] = Path('temp_dir')
) -> os.PathLike:

    dir_name = Path(dir_name)

    try:
        print(f'Making directory {dir_name}...')
        os.mkdir(dir_name)
    except FileExistsError:
        print(f'Directory {dir_name} already exists. Clearing...')
        clear_dir(dir_name)

    print(f'{dir_name} has been created successfully.\n')

    return dir_name


@prints.bounds_printer(
    'Check directory files',
    'Checking has been finished',
)
def print_files(directory: Union[str, os.PathLike]) -> None:

    def raise_an_error(exception_instance):
        raise exception_instance

    try:
        print(f'Scanning directory {directory}')

        for file_list in os.walk(directory, onerror=raise_an_error):
            print(f'In {file_list[0]}:')

            directories = "\n\t\t".join(file_list[1])
            print(f'\tDirectories:\n\t\t{directories}')

            files = "\n\t\t".join(file_list[2])
            print(f'\tFiles:\n\t\t{files}')

    except FileNotFoundError:
        print(f'No such file or directory {directory}...')


def all_files(directory: Union[str, os.PathLike]) -> List[str]:

    directory = Path(directory)
    file_list = []
    file_path = directory

    try:
        for file in os.listdir(directory):
            file_path = directory / file
            if file_path.is_dir():
                sub_dir = all_files(directory / file)
                sub_files = [f'{file}/{sub_file}' for sub_file in sub_dir]
                file_list.extend(sub_files)
            else:
                file_list.append(file)
    except Exception as e:
        print(f"Can't find the {file_path} file.\nReason: {e}")

    return file_list
