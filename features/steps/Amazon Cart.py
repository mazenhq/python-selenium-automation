from behave import *
from selenium.webdriver.common.by import By


#@given("Open amazon Bestsellers page")
#def step_impl(context):
 #   context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@when("Click on Crocs Unisex-Adult")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='a-link-normal']").click()

@when('Input {text} into search amazon field')
def search_for_text(context, text):
    context.app.header.search_for(text)
    context.app.header.click_on_search_icon()




