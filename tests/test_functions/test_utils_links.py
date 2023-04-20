from src.utils import links


def test_return_link():

    url_1 = 'https://www.example.com'
    url_2 = url_1 + '/'
    filename_1 = 'test_file.py'
    filename_2 = '/' + filename_1

    expected = 'https://www.example.com/raw/test_file.py'

    for url in (url_1, url_2):
        for filename in (filename_1, filename_2):
            result = links.return_link(url, filename)
            assert expected == result
