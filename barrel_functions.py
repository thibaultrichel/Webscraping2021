##########################
# Barrel price functions
##########################

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import time


def closePopups(driv):
    driv.implicitly_wait(3)
    driv.find_element_by_id('onetrust-accept-btn-handler').click()
    try:
        wait = WebDriverWait(driv, 15)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'largeBannerCloser'))).click()
    except TimeoutException:
        print('TimeoutException: could not find second popup, timeout and pass')
        pass


def setStartDate(driv, date):
    driv.implicitly_wait(3)
    driv.find_element_by_id('widget').click()
    startDate = driv.find_element_by_id('startDate')
    startDate.clear()
    startDate.send_keys(date)
    driv.find_element_by_id('applyBtn').click()


def getPricesAndDates(driv):
    driv.implicitly_wait(3)
    tab = []
    table = driv.find_elements_by_tag_name('tbody')[1]
    rows = table.find_elements_by_tag_name('tr')
    for row in rows:
        date = row.find_elements_by_tag_name('td')[0].text
        price = float(row.find_elements_by_tag_name('td')[2].text.replace(',', '.'))
        tab.append((date, price))
    return tab


def toDataframe(list_):
    barrelDates = [data[0] for data in list_]
    barrelPrices = [data[1] for data in list_]
    df_barrel = pd.DataFrame(list(zip(barrelDates, barrelPrices)), columns=['Date', 'Prix du barril'])
    return df_barrel


def getBarrelData(driver, date):
    driver.get('https://fr.investing.com/commodities/brent-oil-historical-data')
    time.sleep(4)

    closePopups(driver)
    setStartDate(driver, date)
    time.sleep(2)
    barrel = getPricesAndDates(driver)
    barrelData = toDataframe(barrel)
    driver.close()
    return barrelData
