from typing import List, Union
import os


rep_url = 'https://gitea.radium.group/radium/project-configuration/'

files: List[str] = [
    'nitpick/all.toml',
    'nitpick/darglint.toml',
    'nitpick/editorconfig.toml',
    'nitpick/file-structure.toml',
    'nitpick/flake8.toml',
    'nitpick/isort.toml',
    'nitpick/pytest.toml',
    'nitpick/styleguide.toml',
    'LICENSE',
    'README.md',
]


def return_link(
        rep_url: str, file: Union[str, os.PathLike]
) -> str:
    # Delete extra slashes
    rep_url = rep_url[:-1] if rep_url.endswith('/') else rep_url
    file = file[1:] if file.startswith('/') else file
    return ''.join([rep_url, '/', 'raw', '/', file])
