# -*- coding: utf-8 -*-
from behave import given, when, then

@given('Тап на таб "Меню"')
def tap_menu(context):
    context.app.main_page.tap_menu()

@when('Тап на "Личный кабинет"')
def tap_account(context):
    context.app.menu_page.tap_account()

@then('Пользователь не авторизован, есть кнопка "Войти"')
def sign_in_displayed(context):
    context.app.account_page.sign_in_displayed()

