from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option('detach', True)

driver = Chrome(options)
driver.implicitly_wait(5)

driver.get("https://automated.pythonanywhere.com/login/")

user = driver.find_element(By.NAME, 'username')
user.send_keys("automated")

password = driver.find_element(By.NAME, 'password')
password.send_keys('automatedautomated')

driver.get("https://automated.pythonanywhere.com")
time.sleep(2)
temp = driver.find_element(By.ID, 'displaytimer')
print(f"Average temperature: {temp.text.split(": ")[1]}")