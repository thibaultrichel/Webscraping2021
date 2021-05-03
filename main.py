from selenium import webdriver
from covid_functions import getCovidData
from barrel_functions import getBarrelData


if __name__ == '__main__':
    firstLockdownFrance = '17/03/2020'
    days = 410  # Number of days from the beginning of the 1st lockdown in France
    pathToChromeDriver = '/Users/thibaultrichel/PycharmProjects/chromedriver'

    driver = webdriver.Chrome(pathToChromeDriver)

    covid = getCovidData(driver, 20)
    print(covid)

    barrel = getBarrelData(driver, '11/04/2021')
    print(barrel)

    # actus =
