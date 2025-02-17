from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import pandas

driver = Chrome()
driver.implicitly_wait(5)

driver.get("https://remoteok.com/remote-python-jobs")

locations = []
salaries = []
titles = []
companies = []
urls = []

jobs = driver.find_elements(By.CSS_SELECTOR, '.company_and_position')
for job in jobs:
    tags = job.find_elements(By.CLASS_NAME, 'location')
    tags = [tag.text for tag in tags]
    if len(tags) == 0:
        continue
    for tag in tags:
        if '$' in tag:
            locations.append(tags[0])
            salaries.append(tag)
            titles.append(job.find_element(By.CSS_SELECTOR, 'a h2').text)
            companies.append(job.find_element(By.CSS_SELECTOR, '.companyLink h3').text)
            urls.append(job.find_element(By.CSS_SELECTOR, '.preventLink').get_attribute('href'))

df = pandas.DataFrame({'Title': titles, 'Company': companies, 'Location': locations, 'Salary': salaries, 'URL': urls})
df.to_csv('jobs.csv', index=False)