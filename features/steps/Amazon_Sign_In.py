from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when("Click Orders")
def step_impl(context):
    context.driver.find_element(By.ID, "nav-orders").click()
