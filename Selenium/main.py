from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    consent = driver.find_element(By.CLASS_NAME, 'fc-primary-button')
    consent.click()
    lang = driver.find_element(By.ID, 'langSelect-EN')
    lang.click()
except:
    pass
cookie = driver.find_element(By.ID, 'bigCookie')
while True:
    cookie.click()