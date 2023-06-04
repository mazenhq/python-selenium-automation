from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

ORDER_CLICK = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")


@given('Open amazon main page')
def amazon_main(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.amazon_main.amazon_main()


@when('Click on Order icon')
def click_order(context):
    # context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
    # context.driver.find_element(*ORDER_CLICK).click()
    context.app.header.order_click()


@then('Verify Sign in page shown')
def signin(context):
    # expected_text = 'Sign in'
    # actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    # assert actual_text == expected_text, f'Error! Expected {expected_text} but get {actual_text}'
    context.app.verify_signin.signin()
