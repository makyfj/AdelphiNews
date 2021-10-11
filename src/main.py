import requests
import json
from bs4 import BeautifulSoup

adelphiNewsPage = requests.get("https://www.adelphi.edu/news")

contents = adelphiNewsPage.content

soup = BeautifulSoup(contents, "html.parser")

# retrieves the title of each article in the front page
newsTitle = soup.find_all("span", "news_item_title_link_label")

# number of articles
numberOfNews = len(newsTitle)

# publication date of the article
newsPublicationDate = soup.find_all("time", "news_item_detail_label")

# body of the article
newsBody = soup.find_all("div", "news_item_description")

titles = []
dates = []
bodies = []

for title in newsTitle:
    titles.append(title.string)

for date in newsPublicationDate:
    dates.append(date.string)

for body in newsBody:
    bodies.append(body.p.string)

# To store all articles, to access them easily
articles = [] 

for i in range(numberOfNews):
    articles.append({"title": titles[i], "date": dates[i], "body": bodies[i]})

# How to access the articles
print(articles[0]["title"])
print(articles[0]["date"])
print(articles[0]["body"])


with open("articles.json", 'w') as outfile:
    json.dump(articles, outfile)
    print("Done")
# First article
#for i in range(numberOfNews):
#    print(f"Title: {articles[i][0]}")
#    print(f"Date: {articles[i][1]}")
#    print(f"Body: {articles[i][2]}")
