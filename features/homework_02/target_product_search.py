from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

search_word = 'water'.lower()

# Target search field
# By Xpath
driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']") # //tag[@attr='value']

# search for product

driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys(search_word)

# click the search button

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(4)

text_found = driver.find_element(By.XPATH, "//div[@data-module-type='ListingPageResultsCount']//*[contains(text(), 'water')]")

# verify search results

assert search_word in text_found.text.lower(), f"Expected query not in {search_word}"

driver.quit()