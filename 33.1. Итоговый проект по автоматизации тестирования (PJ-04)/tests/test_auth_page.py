from pages.auth_page import AuthPage
from pages.locators import AuthLocators
import time


def test_PJ_04_1(selenium, driver):
   page = AuthPage(selenium)
   page.btn_click_phone()
   user_name = driver.find_element(*AuthLocators.USER_NAME_INPUT).text
   assert  user_name == "Мобильный телефон"

def test_PJ_04_2(selenium, driver):
   page = AuthPage(selenium)
   page.btn_click_mail()
   user_name = driver.find_element(*AuthLocators.USER_NAME_INPUT).text
   time.sleep(4)
   assert  user_name == "Электронная почта"

def test_PJ_04_3(selenium, driver):
   page = AuthPage(selenium)
   page.btn_click_login()
   user_name = driver.find_element(*AuthLocators.USER_NAME_INPUT).text
   time.sleep(4)
   assert  user_name == "Логин"

def test_PJ_04_4(selenium, driver):
   page = AuthPage(selenium)
   page.btn_click_ls()
   user_name = driver.find_element(*AuthLocators.USER_NAME_INPUT).text
   time.sleep(4)
   assert  user_name == "Лицевой счёт"

def test_PJ_04_5(selenium, driver):
   page = AuthPage(selenium)
   page.btn_click_lost_pass()
   card_title = driver.find_element(*AuthLocators.CARD_TITLE).text
   time.sleep(4)
   assert card_title == "Восстановление пароля"

def test_PJ_04_6(selenium, driver):
   page = AuthPage(selenium)
   page.btn_click_agreement_link()
   time.sleep(4)
   offer_title = driver.find_element(*AuthLocators.OFFER_TITLE).text
   assert offer_title == "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»"

def test_PJ_04_7(selenium, driver):
   page = AuthPage(selenium)
   page.btn_click_register_link()
   card_title = driver.find_element(*AuthLocators.CARD_TITLE).text
   time.sleep(4)
   assert card_title == "Регистрация"

def test_PJ_04_8(selenium, driver):
   page = AuthPage(selenium)
   page.btn_click_faq()
   card_title = driver.find_element(*AuthLocators.FAQ_TITLE).text
   time.sleep(4)
   assert card_title == "Ваш безопасный ключ к сервисам Ростелекома"




