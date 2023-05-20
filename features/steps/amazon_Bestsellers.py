import selectors

from lib2to3.fixes.fix_input import context

from behave import *
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


@given("Open amazon Bestsellers page")
def step_impl(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then("Verify links on the page")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']")
