from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/usr/local/bin/chromedriver')
options = webdriver.ChromeOptions()
options.binary_location = '/opt/google/chrome/google-chrome'
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.example.com')
print(driver.title)
driver.quit()
