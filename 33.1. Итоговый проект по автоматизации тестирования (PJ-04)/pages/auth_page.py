from .base_page import BasePage
from .locators import AuthLocators

import  time,os


class AuthPage(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
       driver.get(url)
       self.phone_btn = driver.find_element(*AuthLocators.PHONE_BTN)
       self.mail_btn = driver.find_element(*AuthLocators.MAIL_BTN)
       self.login_btn = driver.find_element(*AuthLocators.LOGIN_BTN)
       self.ls_btn = driver.find_element(*AuthLocators.LS_BTN)
       self.lost_pas = driver.find_element(*AuthLocators.LOST_PASS)
       self.agreement_link = driver.find_element(*AuthLocators.AGR_LINK)
       self.register_link = driver.find_element(*AuthLocators.REGISTER_LINK)
       self.faq_link = driver.find_element(*AuthLocators.FAQ_LINK)





   def btn_click_phone(self):
       self.phone_btn.click()
   def btn_click_mail(self):
       self.mail_btn.click()
   def btn_click_login(self):
       self.login_btn.click()
   def btn_click_ls(self):
       self.ls_btn.click()
   def btn_click_lost_pass(self):
       self.lost_pas.click()
   def btn_click_agreement_link(self):
       self.agreement_link.click()
   def btn_click_register_link(self):
       self.register_link.click()
   def btn_click_faq(self):
       self.faq_link.click()




   time.sleep(3)