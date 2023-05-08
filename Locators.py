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
driver.get('https://www.amazon.com/')


# By Xpath
#icon
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//span[@class='nav-icon nav-']")
#Need help
driver.find_element(BY.XPATH, "//span[@class='a-expander-prompt']")

#Conditions of use and Privacy Ntice
driver.find_element(By.XPATH, ("//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']"))



# By ID
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'continue')
#forgot password
driver.find_element(BY.ID, 'auth-fpp-link-bottom')
driver.find_element(BY.ID, 'ap-other-signin-issues-link')
driver.find_element(BY.ID, 'createAccountSubmit')

sleep(10)