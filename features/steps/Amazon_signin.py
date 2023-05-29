from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

import features
from features import steps

SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')


@then('Verify Sign In page opens')
def verify_signin_opens(context):
    # Verify URL:
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    # Verify header
    actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    assert actual_text == 'Sign in', f'Expected Sign in header but got {actual_text}'
    # Verify email field present
# 22 changes: 22 additions & 0 deletions22
#features/steps/cart_page.py
#Comment on this file

