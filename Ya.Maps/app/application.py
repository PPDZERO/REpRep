from pages.main_page import MainPage
from pages.menu_page import MenuPage
from pages.account_page import PersonalAccount

class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.menu_page = MenuPage(driver)
        self.account_page = PersonalAccount(driver)