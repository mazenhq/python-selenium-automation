from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Order icon')
def click_order(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

@then('Verify Sign in page shown')
def Verify_sign_in_shown(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_text == expected_text, f'Error! Expected {expected_text} but get {actual_text}'

