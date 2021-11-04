import main as adelphi_news

articles = adelphi_news.articles
titles = adelphi_news.titles
dates = adelphi_news.dates
bodies = adelphi_news.bodies
categories = adelphi_news.categories

title = input("Enter title you looking for: ")

for i in range(len(articles)):
    if title in titles[i]:
        print(bodies[i])
