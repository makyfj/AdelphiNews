import requests
import json
from bs4 import BeautifulSoup

adelphi_news_page = requests.get("https://www.adelphi.edu/news")

contents = adelphi_news_page.content


soup = BeautifulSoup(contents, "html.parser")

# retrieves the title of each article in the front page
news_title = soup.find_all("span", "news_item_title_link_label")

# number of articles
number_of_news = len(news_title)

# publication date of the article
news_publication_date = soup.find_all("time", "news_item_detail_label")

# body of the article
news_body = soup.find_all("div", "news_item_description")

# category of the article
news_category = soup.find_all("li", "news_item_category" )


titles = []
dates = []
bodies = []
categories = []

for title in news_title:
    titles.append(title.string)

for date in news_publication_date:
    dates.append(date.string)

for body in news_body:
    bodies.append(body.p.string)


for category in news_category:
    # for ul - news_item_category_list
    # categories.append({"category": [", ".join((category.text).strip("\n").split("\n\n\n"))]})
    categories.append({"category": category.text.strip("\n")})


# To store all articles, to access them easily
articles = [] 

for i in range(number_of_news):
    articles.append({"title": titles[i],"category": categories[i] ,"date": dates[i], "body": bodies[i]})

# How to access the articles
# print(articles[0]["title"])
# print(articles[0]["date"])
# print(articles[0]["body"])


with open("articles.json", 'w') as outfile:
    json.dump(articles, outfile)
    print("Adelphi news articles downloaded")
