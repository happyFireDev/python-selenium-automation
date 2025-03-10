from selenium import webdriver
from selenium.webdriver.common import by
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
driver.get('https://www.target.com/ ')


# Click SignIn button
driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]").click()

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

sleep(4)

# Confirm "Sign into your Target account” text is shown
driver.find_element(By.XPATH, "//h1[span='Sign into your Target account']")

# SignIn button is shown
driver.find_element(By.ID, "login")

# close driver

driver.quit()
