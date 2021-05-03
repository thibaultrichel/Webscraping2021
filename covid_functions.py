######################
# Covid-19 functions
######################

import time
import pandas as pd


def covid_goPreviousDay(driver):
    reportNav = driver.find_element_by_class_name('report-nav')
    button = reportNav.find_element_by_tag_name('svg')
    button.click()


def covid_getTodayDate(driver):
    header = driver.find_element_by_class_name('menu-header')
    text = header.find_element_by_tag_name('h3').text
    date = text.split(' ')[2]
    return date


def covid_getNbCases(driver):
    nbCases = driver.find_elements_by_class_name('counter-container')
    for container in nbCases:
        if "cas confirmés" in container.text:
            value = nbCases[0].find_element_by_class_name('value').text
            return int(value.replace(' ', ''))
    return None


def covid_getNbDeaths(driver):
    nbDoses = driver.find_elements_by_class_name('counter-container')
    for container in nbDoses:
        if "cumul des décès" in container.text:
            value = nbDoses[2].find_element_by_class_name('value').text
            return int(value.replace(' ', ''))
    return None


def covid_toDataframe(datesList, casesList, deathsList):
    df_covid = pd.DataFrame(data=list(zip(datesList, casesList, deathsList)),
                            columns=['Date', 'NbCases', 'NbDeaths'])
    return df_covid


def getCovidData(driver, days):
    driver.get('https://dashboard.covid19.data.gouv.fr/vue-d-ensemble?location=FRA')
    time.sleep(3)

    covid_goPreviousDay(driver)  # Always start from the previous day, otherwise data is not updated

    data = []
    for i in range(days):
        date = covid_getTodayDate(driver)
        cases = covid_getNbCases(driver)
        injections = covid_getNbDeaths(driver)

        data.append([date, cases, injections])

        covid_goPreviousDay(driver)

    datesList = [row[0] for row in data]
    casesList = [row[1] for row in data]
    deathsList = [row[2] for row in data]

    df_covid = covid_toDataframe(datesList, casesList, deathsList)
    return df_covid
