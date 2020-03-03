from selenium.webdriver.common.by import By

from pages.base_page import Page

class MainPage(Page):
    TAB_MENU = (By.ID, 'ru.yandex.yandexmaps.debug:id/tab_navigation_tab_menu')

    def tap_menu(self):
        self.click(*self.TAB_MENU)