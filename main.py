from selenium import webdriver
from covid_functions import getCovidData
from barrel_functions import getBarrelData
from news_functions import getNewsData
import pandas as pd
from datetime import datetime
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 17)


def getFinalDataframe(covidDF, barrelDF, newsDF, writeToCsv=False):
    temp_DF = pd.merge(covidDF, barrelDF, how='outer')
    DF = pd.merge(temp_DF, newsDF, how='outer')

    # Sorting by date
    DF['Date'] = pd.to_datetime(DF['Date'], format='%d/%m/%Y')
    DF = DF.sort_values(by=['Date'], ascending=False)

    # Filling NaNs in 'BarrelPrice' by making the mean between previous and next values
    DF['BarrelPrice'] = pd.concat([DF['BarrelPrice'].ffill(), DF['BarrelPrice'].bfill()]).groupby(level=0).mean()

    # Dropping rows where 'BarrelPrice' or 'NbCases' or 'NbDeaths' value is NaN
    DF = DF.dropna(subset=['BarrelPrice'])
    DF = DF.dropna(subset=['NbCases'])
    DF = DF.dropna(subset=['NbDeaths'])

    # Limiting to 2 decimals every value of 'BarrelPrice' column
    DF['BarrelPrice'] = DF['BarrelPrice'].apply(lambda x: "{:.2f}".format(x))

    # Dropping every row where date is duplicated, because of getting multiple news titles for the same day
    DF = DF.drop_duplicates(subset='Date', keep="first")

    if writeToCsv:
        DF.to_csv('dftest.csv', index=False)

    return DF


if __name__ == '__main__':
    firstLockdownFrance = '17/03/2020'
    days = 410  # Number of days from the beginning of the 1st lockdown in France
    pathToChromeDriver = '/Users/thibaultrichel/PycharmProjects/chromedriver'
    driver = webdriver.Chrome(pathToChromeDriver)

    total_startTime = datetime.now()

    print(f"💬 Fetching Covid-19 data of {days} days...")
    covid_startTime = datetime.now()
    covid = getCovidData(driver, days)
    covid_endTime = datetime.now()
    covid_execTime = covid_endTime - covid_startTime
    print(f"✨ Done in {covid_execTime}")

    print(f"\n💬 Fetching Barrel data from {firstLockdownFrance}...")
    barrel_startTime = datetime.now()
    barrel = getBarrelData(driver, firstLockdownFrance)
    barrel_endTime = datetime.now()
    barrel_execTime = barrel_endTime - barrel_startTime
    print(f"✨ Done in {barrel_execTime}")

    print(f"\n💬 Fetching News data from {firstLockdownFrance}...")
    news_startTime = datetime.now()
    news = getNewsData(33)
    news_endTime = datetime.now()
    news_execTime = news_endTime - news_startTime
    print(f"✨ Done in {news_execTime}")

    total_endTime = datetime.now()
    total_execTime = total_endTime - total_startTime
    print(f"\n✅ Fetching all data done in {total_execTime}")

    df = getFinalDataframe(covid, barrel, news, writeToCsv=True)
    print(f"\n\n{df}")
