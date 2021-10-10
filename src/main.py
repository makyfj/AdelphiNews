import requests
from bs4 import BeautifulSoup

adelphiNewsPage = requests.get("https://www.adelphi.edu/news")

contents = adelphiNewsPage.content

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

pageTitle = soup.title
