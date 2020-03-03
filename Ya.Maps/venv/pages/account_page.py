from selenium.webdriver.common.by import By
from pages.base_page import Page

class PersonalAccount(Page):
    SIGN_IN_BUTTON = (By.ID,'ru.yandex.yandexmaps.debug:id/sign_in_button')
    LOGIN_EDIT = (By.ID, 'ru.yandex.yandexmaps.debug:id/edit_login')
    LOGIN_NEXT = (By.ID, 'ru.yandex.yandexmaps.debug:id/button_next')
    PASSWORD_EDIT = (By.ID, 'ru.yandex.yandexmaps.debug:id/edit_password')
    AVATAR_ACCOUNT = (By.ID, 'ru.yandex.yandexmaps.debug:id/avatar_image')
    USERNAME_ACC = (By.ID, 'ru.yandex.yandexmaps.debug:id/username')

    def input_login(self, account_login:str):
        self.input(account_login, *self.LOGIN_EDIT)

    def tap_sign_in(self):
        self.click(*self.SIGN_IN_BUTTON)

    def tap_login_edit(self):
        self.click(*self.LOGIN_EDIT)

    def tap_login_next(self):
        self.click(*self.LOGIN_NEXT)

    def tap_password_edit(self):
        self.click(*self.PASSWORD_EDIT)

    def input_password(self, account_password:str):
        self.input(account_password, *self.PASSWORD_EDIT)

    def sign_in_displayed(self):
        self.is_displayed(*self.SIGN_IN_BUTTON)

    def log_in_displayed(self):
        self.is_displayed(*self.LOGIN_EDIT)

    def verify_log_in(self, account_login: str):
        result_text = self.find_element(*self.USERNAME_ACC).text
        assert account_login in result_text, f'Логин {account_login} совпадает с отобразившимся {result_text}'