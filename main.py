from selenium import webdriver
from covid_functions import getCovidData
from barrel_functions import getBarrelData
from news_functions import getNewsData
import pandas as pd


def getFinalDataframe(covidDF, barrelDF, newsDF, writeToCsv=False):
    temp_DF = pd.merge(covidDF, barrelDF, how='outer')
    temp_DF.fillna('None', inplace=True)

    DF = pd.merge(temp_DF, newsDF, how='outer')
    DF.fillna('None', inplace=True)

    DF['Date'] = pd.to_datetime(DF['Date'], format='%d/%m/%Y')
    sortedDF = DF.sort_values(by=['Date'], ascending=False)

    if writeToCsv:
        sortedDF.to_csv('dftest.csv', index=False)

    return sortedDF


if __name__ == '__main__':
    firstLockdownFrance = '17/03/2020'
    days = 410  # Number of days from the beginning of the 1st lockdown in France
    pathToChromeDriver = '/Users/thibaultrichel/PycharmProjects/chromedriver'
    driver = webdriver.Chrome(pathToChromeDriver)

    covid = getCovidData(driver, 30)
    barrel = getBarrelData(driver, '01/04/2021')
    news = getNewsData(2)

    df = getFinalDataframe(covid, barrel, news, writeToCsv=False)
    print(df)
