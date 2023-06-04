from selenium.webdriver.common.by import By
from Pages.base_page import Page

class Header(Page):
    ORDER_CLICK = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")

    def order_click(self):
        self.click(*self.ORDER_CLICK)
