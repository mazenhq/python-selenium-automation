from Pages.base_page import Page

class MainPage(Page):

    def amazon_main(self):
        self.open_url('https://www.amazon.com')