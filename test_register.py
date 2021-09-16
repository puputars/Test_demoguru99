import pytest
import selenium
import re
from selenium.webdriver.support.ui import Select
import time

from BaseClass import BaseClass
from pageObjects.RegisterPage import RegisterPage
from pageObjects.RegisterSuccessPage import RegisterSuccessPage

from manage_data import manage_data

@pytest.mark.usefixtures("setup")
class Test_Register(BaseClass):

  def test_register(self):

    
    log = self.getLogger()
    register_page = RegisterPage(self.driver)
    register_success = RegisterSuccessPage(self.driver)
    log.info(register_page.title())
    #register_page.screenshot(register_page.title())

    filename = "file_csv/data.csv"
    total_data = manage_data().total_file(filename)
    data = manage_data().read_file(filename)
    log.info("Total Data = {}".format(total_data))
    for no in range(total_data):
      log.debug(no)
      #register_page.submit()

      log.info("firstname = {}".format(data["first_name"][no]))
      register_page.first_name().send_keys(data["first_name"][no])
      log.info("lastname = {}".format(data["last_name"][no]))
      register_page.last_name().send_keys(data["last_name"][no])
      log.info("phone = {}".format(data["phone"][no]))
      register_page.phone().send_keys(data["phone"][no])
      log.info("email = {}".format(data["email"][no]))
      register_page.email().send_keys(data["email"][no])
      log.info("address = {}".format(data["address"][no]))
      register_page.address().send_keys(data["address"][no])
      log.info("city = {}".format(data["city"][no]))
      register_page.city().send_keys(data["city"][no])
      log.info("state = {}".format(data["state"][no]))
      register_page.state().send_keys(data["state"][no])
      log.info("postal_code = {}".format(data["postal_code"][no]))
      register_page.postal_code().send_keys(data["postal_code"][no])
      log.info("country = {}".format(data["country"][no]))
      register_page.country().send_keys(data["country"][no])
      log.info("username = {}".format(data["user_name"][no]))
      register_page.user_name().send_keys(data["user_name"][no])
      log.info("password = {}".format(data["password"][no]))
      register_page.password().send_keys(data["password"][no])
      log.info("confirm password = {}".format(data["confirm_password"][no]))
      register_page.confirm_password().send_keys(data["confirm_password"][no])

      register_page.submit()
      log.info("succesfully register")
      register_success.back_to_register().click()

        

      

