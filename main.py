from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

website = 'https://www.copart.com/'
path = '/Users/shiggy/Downloads/chromedriver_mac_arm64 (1)/chromedriver'

chrome_options = Options()

chrome_options.binary_location = '/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(website)

time.sleep(50)

driver.quit()