# AdelphiNews - Scraper

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

You might need to create a virtual environment to install these modules.
[Python Virtual environment](https://docs.python.org/3/library/venv.html)
