import yagmail
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)

driver = Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
consent = driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
consent.click()

price_drop = driver.find_element(By.CLASS_NAME, 'stock-trend').text
price_drop = float(price_drop.split()[0])
if price_drop <= -0.1:
    time.sleep(1)
    driver.save_screenshot('price_drop.png')
    connection = yagmail.SMTP("iamandrewtech@gmail.com", 'password123')
    connection.send("iamandrewtech@gmail.com", 'NEW PRICE DROP 🤯😲🤯', f'NEW PRICE DROP OF {price_drop}%! CAN YOU BELIEVE THAT? I, FOR ONE, CANNOT!', attachments='price_drop.png')