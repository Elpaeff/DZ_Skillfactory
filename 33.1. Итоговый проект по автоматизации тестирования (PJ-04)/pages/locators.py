from symtable import Class

from selenium.webdriver.common.by import By

class AuthLocators:
    PHONE_BTN = (By.ID, "t-btn-tab-phone")
    MAIL_BTN = (By.ID, "t-btn-tab-mail")
    LOGIN_BTN = (By.ID, "t-btn-tab-login")
    LS_BTN = (By.ID, "t-btn-tab-ls")
    USER_NAME_INPUT = (By.CLASS_NAME, "rt-input__placeholder")
    LOST_PASS = (By.ID, "forgot_password")
    CARD_TITLE = (By.ID, "card-title")
    RESET_BACK = (By.ID, "reset-back")
    AGR_LINK = (By.ID, "rt-auth-agreement-link")
    OFFER_TITLE = (By.CLASS_NAME, "offer-title")
    REGISTER_LINK = (By.ID, "kc-register")
    FAQ_LINK = (By.ID,"faq-open")
    FAQ_TITLE= (By.CLASS_NAME,"faq - modal__title")

class RegLocators:
    FORM_USER_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    FORM_USER_LAST_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    WEB_FORM = (By.XPATH, '//*[@id="page-right"]/div')
    ERROR_TEXT_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span')
    ERROR_TEXT_LAST_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span')





