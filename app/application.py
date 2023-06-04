from Pages.header import Header
from Pages.amazon_main import MainPage
from Pages.verify_signin import VerifySignin


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.amazon_main = MainPage(self.driver)
        self.verify_signin = VerifySignin(self.driver)



