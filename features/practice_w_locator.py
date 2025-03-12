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
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=64NBPX3SCT41VWJP4415&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


# Amazon logo
# By Xpath
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']") # //tag[@attr='value']

# Create Account text
# by css selector
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Email field
driver.find_element(By.ID, "ap_email") # //tag[@attr='value']

# Continue button
driver.find_element(By.XPATH, "//input[@id='continue']") # //tag[@attr='value']

# Conditions of use link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt' and contains(text(), 'Need help?')]")

# Forgot your password link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom' and contains(text(), 'Forgot your password')]")

# Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

sleep(3)

driver.quit()