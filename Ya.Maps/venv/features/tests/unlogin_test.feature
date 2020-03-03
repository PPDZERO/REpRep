# Created by ruslan-sab at 17/02/2020
Feature: При чистом запуске пользователь не авторизован
  # Enter feature description here

  Scenario: Юзер не авторизован в личном кабинете
    Given Тап на таб "Меню"
    When Тап на "Личный кабинет"
    Then Пользователь не авторизован, есть кнопка "Войти"