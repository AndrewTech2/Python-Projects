from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://tinder.onelink.me/9K8a/3d4abb81")

login = driver.find_element(By.XPATH, '//*[@id="q18919352"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login.click()

fb_login = driver.window_handles[1]
driver.switch_to.window(fb_login)

email = driver.find_element(By.NAME, 'email')
email.send_keys("iamandrewtech@gmail.com")

password = driver.find_element(By.NAME, 'pass')
password.send_keys("password123")

submit = driver.find_element(By.NAME, 'login')
submit.click()

input("Press any button to commence after accepting on the FB page > ")

driver.switch_to.window(driver.window_handles[0])

location = driver.find_element(By.XPATH, '//*[@id="q18919352"]/div/div[1]/div/div/div[3]/button[1]')
location.click()

notification = driver.find_element(By.XPATH, '//*[@id="q18919352"]/div/div[1]/div/div/div[3]/button[2]')
notification.click()

time.sleep(3)
reject = driver.find_element(By.XPATH, '//*[@id="q1747300428"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')
while True:
    try:
        reject.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        home = driver.find_element(By.XPATH, '//*[@id="q18919352"]/div/div/div[2]/button[2]')
        home.click()