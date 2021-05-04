import pandas as pd
from selenium import webdriver
from covid_functions import getCovidData
from barrel_functions import getBarrelData
from news_functions import getNewsData
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 17)

# driver = webdriver.Chrome('/Users/thibaultrichel/PycharmProjects/chromedriver')
#
# covidDF = getCovidData(driver, 30)
# barrelDF = getBarrelData(driver, '01/04/2021')
# newsDF = getNewsData(3)
#
# temp_DF = pd.merge(covidDF, barrelDF, how='outer')
# temp_DF.fillna('None', inplace=True)
#
# DF = pd.merge(temp_DF, newsDF, how='outer')
# DF.fillna('None', inplace=True)
#
# DF['Date'] = pd.to_datetime(DF['Date'], format='%d/%m/%Y')
# sortedDF = DF.sort_values(by=['Date'], ascending=False)
# sortedDF.reset_index(inplace=True)
# sortedDF.to_csv('dftest.csv')
#
# print(sortedDF)
