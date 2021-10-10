import requests
from bs4 import BeautifulSoup

adelphiNewsPage = requests.get("https://www.adelphi.edu/news")

contents = adelphiNewsPage.content

soup = BeautifulSoup(contents, "html.parser")

# retrieves the title of each article in the front page
newsTitle = soup.find_all("span", "news_item_title_link_label")

# publication date of the article
newsPublicationDate = soup.find_all("time", "news_item_detail_label")

# body of the article
newsBody = soup.find_all("div", "news_item_description")

# number of articles in the front page
articles = len(newsTitle)
print(articles)

# for body in newsBody:
#    print(body.p.string)

# for date in newsPublicationDate:
#     print(date.string)

# prints the title of the article
# for title in newsTitle:
#     print(title.string)
