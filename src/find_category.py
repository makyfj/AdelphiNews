import main as adelphi_news

articles = adelphi_news.articles
# categories = adelphi_news.categories
# titles = adelphi_news.titles

user_input = input("Enter category: ").lower()

# for article in articles:
#     # for i in article['category']:
#         # if user_input == (article[i]['category']):
#         #     print(article[i]['title'])

# for category in categories:
    # if user_input == category['category']:

# for title in titles:
#     print(title)

for i in range(len(articles)):

    if user_input == articles[i]['category']['category']:
        print(articles[i]['title'])
    # print(articles[i]['category']['category'])
