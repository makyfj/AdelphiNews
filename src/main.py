import requests
from bs4 import BeautifulSoup

adelphi_news_page = requests.get("https://www.adelphi.edu/news")

contents = adelphi_news_page.content

soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify())
