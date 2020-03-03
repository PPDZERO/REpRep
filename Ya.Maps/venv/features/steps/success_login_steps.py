# -*- coding: utf-8 -*-
from behave import given, when, then

@given('Пользователь переходит во вкладку личный кабинет')
def tap_menu(context):
    context.app.main_page.tap_menu()
    context.driver.implicitly_wait(2)
@when('Нажимает кнопку "Личный кабинет"')
def tap_account(context):
    context.app.menu_page.tap_account()

@when('Нажимает кнопку "Войти"')
def tap_sign_in(context):
    context.app.account_page.tap_sign_in()
    context.driver.implicitly_wait(3)

@when('Нажимает на поле логина')
def tap_login_edit(context):
    context.app.account_page.tap_login_edit()

@when('вводит валидный логин {account_login} в поле логина')
def input_login(context, account_login):
    context.app.account_page.input_login(account_login)

@when('нажимает далее')
def tap_login_next(context):
    context.app.account_page.tap_login_next()
    context.driver.implicitly_wait(3)

@when('нажимает на поле пароля')
def tap_password_edit(context):
    context.app.account_page.tap_password_edit()

@when('вводит валидный пароль {account_password}')
def input_password(context, account_password):
    context.app.account_page.input_password(account_password)

@when('нажимает войти')
def tap_login_next(context):
    context.app.account_page.tap_login_next()

@then('Пользователь успешно авторизовался под {account_login}')
def verify_log_in(context, account_login):
    context.app.account_page.verify_log_in(account_login)