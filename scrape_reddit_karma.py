## Script to get reddit karma count with selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge('/Program Files/edgedriver_win64/msedgedriver')
driver.get('https://reddit.com/u/psilvs')
time.sleep(1)

driver.maximize_window()

try:
    print(driver.find_element_by_id('profile--id-card--highlight-tooltip--karma').text)
except:
    driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div[1]/div/div/div[2]/button').click()
    time.sleep(1)
    print(driver.find_element_by_id('profile--id-card--highlight-tooltip--karma').text)