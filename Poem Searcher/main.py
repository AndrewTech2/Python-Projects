from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option('detach', True)

driver = Chrome(options=option)
driver.implicitly_wait(5)

driver.get('https://poetii-nostri.ro/dimitrie-anghel-autor-47/')
urls = driver.find_elements(By.CSS_SELECTOR, '.product-col-1 a')
urls = list(map(lambda x: x.get_attribute('href'), urls))

for url in urls:
    driver.get(url)
    text = driver.find_element(By.CSS_SELECTOR, ".pagerrr p").text
    if 'Doamne' in text:
        print(url)