from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

@given('Open amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')



@when('Click on Cart icon')
def click_Cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()



@then('Verify Cart is empty')
def Verify_cart_is_empty(context):
    expected_text = 'Your Amazon Cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert actual_text == expected_text, f'Error! Expected {expected_text} but get {actual_text}'

