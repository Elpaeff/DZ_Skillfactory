from pages.reg_page import RegPage
from pages.locators import AuthLocators
from pages.locators import RegLocators

import time

def test_PJ_04_13_more_30_kir(selenium, driver):
    page = RegPage(selenium)
    page.btn_click_register_link()
    input_user_name = driver.find_element(*RegLocators.FORM_USER_NAME)
    web_form = driver.find_element(*RegLocators. WEB_FORM )
    input_user_name.send_keys("фффывфаппывывааывываываываывпыпыпыпвыаываываыаываыывыаываыавраоо")
    web_form.click()
    error_text = driver.find_element(*RegLocators. ERROR_TEXT_NAME).text
    assert error_text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

def test_PJ_04_13_min_1_kir(selenium, driver):
    page = RegPage(selenium)
    page.btn_click_register_link()
    input_user_name = driver.find_element(*RegLocators.FORM_USER_NAME)
    web_form = driver.find_element(*RegLocators. WEB_FORM )
    input_user_name.send_keys("ф")
    web_form.click()
    error_text = driver.find_element(*RegLocators. ERROR_TEXT_NAME).text
    assert error_text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

def test_PJ_04_14(selenium, driver):
    page = RegPage(selenium)
    page.btn_click_register_link()
    input_user_name = driver.find_element(*RegLocators.FORM_USER_NAME)
    web_form = driver.find_element(*RegLocators. WEB_FORM )
    input_user_name.send_keys("фfgdgfdg1")
    web_form.click()
    error_text = driver.find_element(*RegLocators. ERROR_TEXT_NAME).text
    assert error_text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_PJ_04_15(selenium, driver):
    page = RegPage(selenium)
    page.btn_click_register_link()
    input_user_name = driver.find_element(*RegLocators.FORM_USER_LAST_NAME)
    web_form = driver.find_element(*RegLocators.WEB_FORM)
    input_user_name.send_keys("фfgdgfdg1")
    web_form.click()
    error_text = driver.find_element(*RegLocators.ERROR_TEXT_LAST_NAME).text
    assert error_text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."




