from .base_page import BasePage
from .locators import RegLocators
from .locators import AuthLocators

import  time,os


class RegPage(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
       driver.get(url)
       self.register_link = driver.find_element(*AuthLocators.REGISTER_LINK)
   def btn_click_register_link(self):
       self.register_link.click()

   time.sleep(4)
   def reg_form(self, driver):
       self.form_user_name = driver.find_element(*RegLocators. FORM_USER_NAME)
       self.form_user_last_name = driver.find_element(*RegLocators. FORM_USER_LAST_NAME)

