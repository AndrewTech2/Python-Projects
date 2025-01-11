from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

default_up = 10
default_down = 150

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)

def get_speed():
    driver.get("https://www.speedtest.net")

    consent = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    consent.click()

    go = driver.find_element(By.CLASS_NAME, 'js-start-test')
    go.click()

    time.sleep(60)

    global down
    down = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    print(down)

    global up
    up = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    print(up)
def tweet():
    driver.get("https://twitter.com/i/flow/signup")

    login = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/button')
    login.click()

    email = driver.find_element(By.NAME, 'text')
    email.send_keys("anatomiacorpuluiuman@gmail.com")

    next = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
    next.click()

    password = driver.find_element(By.NAME, 'password')
    password.send_keys("Buhuta2010")

    complete = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
    complete.click()

    text_box = driver.find_element(By.CLASS_NAME, 'public-DraftEditor-content')
    text_box.send_keys(f"Hey Internet Provider, this is my speed: {down} mbps (download speed); {up} (upload speed). My plan is {default_down} mbps (download) and {default_up} mbps (upload). What is this?!")

    send = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    send.click()

get_speed()
tweet()