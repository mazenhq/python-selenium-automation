from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from Pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    ORDER_CLICK = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    DEPT_SELECT = (By.ID, 'searchDropdownBox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    Search_FOR = (By.ID, 'twotabsearchtextbox')
    Computers_Submenu = (By.CSS_SELECTOR, "[data-category='computers']")
    NEW_ARRIVAL = (By.XPATH, "//span[(@class='nav-a-content') and contains(text(), 'New Arrivals')]")
    ALL_DEALS = (By.XPATH, "//a[@class='mm-merch-panel']//ul[@class='mm-category-list']/li/h3")
    def order_click(self):
        self.click(*self.ORDER_CLICK)

    def select_dept(self):
        dept_select = self.find_element(*self.DEPT_SELECT)
        select = Select(dept_select)
        select.select_by_value('search-alias=fashion')

    def select_computer_dept(self):
        dept_select = self.find_element(*self.DEPT_SELECT)
        select = Select(dept_select)
        select.select_by_value('search-alias=computers')

    def amazon_fashion(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')
    def search_for(self, text):
       self.input_text(text, *self.Search_FOR)

    def click_on_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def hover_new_arrivals(self):
        hover_new_arrivals = self.find_element(*self.NEW_ARRIVAL)

        actions = ActionChains(self.driver)
        actions.move_to_element(hover_new_arrivals)
        actions.perform()
        sleep(5)

    def verify_dept(self, dep):
        self.verify_url_contains_query(dep)
        # self.wait_for_element_appear(*self.Computers_Submenu)

    def verify_deals(self):
        deals = self.find_elements(*self.ALL_DEALS)
        deals = deals[9:]
        for deal in deals:
            assert deal.text in ['Women', 'Men', 'Girls', 'Boys', 'Baby', 'Luggage'], f"Unexpected Category found: {deal.text}"




