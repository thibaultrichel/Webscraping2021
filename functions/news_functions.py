from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
import locale
import pandas as pd
locale.setlocale(locale.LC_TIME, "fr_FR")


def news_handleDate(strDate):
    dateOk = strDate[:-6]
    date = datetime.strptime(dateOk, '%A %d %B %Y')
    return date.strftime('%d/%m/%Y')


def news_getNewsTitles(nbPage):
    url = 'https://www.leguideboursier.com/actualite-boursiere/matieres-premieres/petrole.php?p=' + str(nbPage)
    time.sleep(10)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    center = soup.find(class_='text-left')
    articles = center.find_all(class_='article-list')
    titles = []
    for art in articles:
        title = art.find('h2')
        date = art.find(class_='time')
        if title and date:
            titles.append((title.text, news_handleDate(date.text)))

    return titles


def news_toDataframe(list_):
    newsTitles = [data[0] for data in list_]
    newsDates = [data[1] for data in list_]
    df_barrel = pd.DataFrame(list(zip(newsDates, newsTitles)), columns=['Date', 'News Titles'])
    return df_barrel


def getNewsData(nbPages):
    titlesByPages = []
    for p in range(1, nbPages+1):
        print(f"Fetching news from page n°{p}/{nbPages}...")
        titlesByPages.append(news_getNewsTitles(p))

    allTitles = [item for page in titlesByPages for item in page]
    news = news_toDataframe(allTitles)
    return news
