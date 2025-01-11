from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.NAME, 'username')
username.send_keys('tomsmith')
password = driver.find_element(By.NAME, 'password')
password.send_keys('SuperSecretPassword!')
login = driver.find_element(By.TAG_NAME, 'button')
login.click()