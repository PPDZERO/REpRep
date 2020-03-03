# -*- coding: utf-8 -*-
from behave import given, when, then

@given('Пользователь переходит во вкладку личный кабинет')
def tap_menu(context):
    context.app.main_page.tap_menu()

def

@when('Нажимает кнопку "Войти"')
def tap_account(context):
    context.app.menu_page.tap_account()

@then('Пользователь успешно авторизовался')
def sign_in_displayed(context):
    context.app.account_page.sign_in_displayed()