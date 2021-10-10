import requests
from bs4 import BeautifulSoup

adelphiNewsPage = requests.get("https://www.adelphi.edu/news")

contents = adelphiNewsPage.content

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

pageTitle = soup.title

# retrieves the title of each article in the front page
newsTitle = soup.find_all("span", "news_item_title_link_label")

# prints the title of the article
for title in newsTitle:
    print(title.string)
