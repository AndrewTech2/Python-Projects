from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime

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

with open(f"{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.txt", 'w') as file:
    file.write(f"{temp.text.split(': ')[1]}")

driver.get('https://titan22.com/account/login')

email = driver.find_element(By.NAME, 'customer[email]')
email.send_keys("iamandrewtech@gmail.com")

password = driver.find_element(By.NAME, 'customer[password]')
password.send_keys('AdeninaTiminaCitozinaGuanina')

sign_in = driver.find_element(By.XPATH, '/html/body/main/article/section/div/div[1]/form/button')
sign_in.click()

contact = driver.find_element(By.XPATH, '/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a')
contact.click()