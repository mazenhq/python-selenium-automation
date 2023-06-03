from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

NOTICE_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")



@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)
    print('All windows:', context.driver.window_handles)

@step("Click on Amazon Privacy Notice link")
def click_link(context):
     context.driver.find_element(*NOTICE_LINK).click()


@step("Switch to the newly opened window")
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print('After window opened, all windows', all_windows)
    context.driver.switch_to.window(all_windows[1])


@then("Verify Amazon Privacy Notice page is opened")
def verify_privacy_opens(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))


@step("User can close new window and switch back to original")
def close_blog(context):
    context.driver.close()
    #switch to original window
    context.driver.switch_to.window(context.original_window)


