from bs4 import BeautifulSoup
import requests
import time


def getNewsTitles(nbPage):
    url = 'https://www.leguideboursier.com/actualite-boursiere/matieres-premieres/petrole.php?p=' + str(nbPage)
    time.sleep(10)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    articles = soup.find_all('li')
    titles = []

    return titles


allTitles = [getNewsTitles(p) for p in range(1, 4)]
for pa in allTitles:
    print(pa)
