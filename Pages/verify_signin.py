from selenium.webdriver.common.by import By
from Pages.base_page import Page

class VerifySignin(Page):
    RESULT_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def signin(self):
        expected_text = 'Sign in'
        actual_text = self.driver.find_element(*self.RESULT_TEXT).text
        assert actual_text == expected_text, f'Error! Expected {expected_text} but get {actual_text}'
