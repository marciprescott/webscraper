"""A webscraper program"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


web = "https://www.audible.com/search"
path = "/Users/marciprescott/Downloads/chromedriver-mac-arm64/chromedriver"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
# Open chromedriver and open website
driver.get(web)
