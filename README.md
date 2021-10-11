# AdelphiNews - Scraper

Make sure to install these packages in a virtual environment, otherwise it might break your python installation.

Windows
[Python Virtual environment](https://docs.python.org/3/library/venv.html)

If you are in a mac:
[Mac installation virtual environment](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html)

Once virtual environment installed:

- source env/bin/activate
- pip install beautifulsoup4
- pip install requests

You'll be working on the AdelphiNews Environment

## Tools to be used to Get and Clean data

- [Requests](https://docs.python-requests.org/en/master/user/quickstart/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Requests

Quick example how to use it:

```
import requests

page = requests.get('http://examplesite.com')

contents = page.content`

```

## BeautifulSoup

Quick example:

```
from bs4 import BeautifulSoup

soup = BeautifulSoup(contents, 'html.parser')

soup.find_all('a')

```
