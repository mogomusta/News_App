from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.


def index(request):
    api = NewsApiClient(api_key='d30c5c268e194e7fa7f6c38ef6da76a0')
    headLines = api.get_top_headlines(sources='al-jazeera-english')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'main/index.html', context={'mylist': mylist})
