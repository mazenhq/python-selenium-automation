from behave import *
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@When('Select department computers')
def select_dept(context):
    context.app.header.select_computer_dept()
@When('Search for PC')
def search_PC(context):
    context.app.header.search_for()
@Then('Verify correct {dep} department shown by the url')
def verify_dept_shown(context, dep):
    context.app.header.verify_dept(dep)


@then("Verify user sees the deals")
def step_impl(context):
    context.app.header.verify_deals()