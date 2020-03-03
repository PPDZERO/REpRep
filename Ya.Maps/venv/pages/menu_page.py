from selenium.webdriver.common.by import By

from pages.base_page import Page

class MenuPage(Page):
    PERSONAL_ACCOUNT = (By.ID, 'ru.yandex.yandexmaps.debug:id/main_menu_cabinet_button')

    def tap_account(self):
        self.click(*self.PERSONAL_ACCOUNT)