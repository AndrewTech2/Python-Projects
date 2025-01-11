from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://linkedin.com/login")
driver.maximize_window()

username = driver.find_element(By.ID, "username")
username.send_keys("iamandrewtech@gmail.com")

password = driver.find_element(By.ID, 'password')
password.send_keys("Buhuta2010")

submit = driver.find_element(By.CLASS_NAME, 'from__button--floating')
submit.click()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4053823796&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

close = driver.find_element(By.ID, 'ember45')
close.click()

links = driver.find_elements(By.CLASS_NAME, 'job-card-container__link')
links_list = []
for link in links:
    links_list.append(link.get_attribute("href"))

for link in links_list:
    driver.get(link)
    save = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div/div/main/div[2]/div[1]/div/div[1]/div/div/div/div[5]/div/button')
    save.click()
    time.sleep(2)