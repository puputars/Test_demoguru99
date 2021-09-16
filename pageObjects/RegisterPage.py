
from pageObjects.RegisterSuccessPage import RegisterSuccessPage


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        
    
    def title(self):
        title = self.driver.title
        return title

    def first_name(self):
        return self.driver.find_element_by_name("firstName")

    def last_name(self):
        return self.driver.find_element_by_name("lastName") 

    def phone(self):
        return self.driver.find_element_by_name("phone")

    def email(self):
        return self.driver.find_element_by_name("userName")  
    
    def address(self):
        return self.driver.find_element_by_name("address1")

    def city(self):
        return self.driver.find_element_by_name("city") 

    def state(self):
        return self.driver.find_element_by_name("state") 

    def postal_code(self):
        return self.driver.find_element_by_name("postalCode") 

    def country(self):
        return self.driver.find_element_by_name("country")

    def user_name(self):
        return self.driver.find_element_by_name("email") 

    def password(self):
        return self.driver.find_element_by_name("password") 
    
    def confirm_password(self):
        return self.driver.find_element_by_name("confirmPassword") 

    def submit(self):
        return self.driver.find_element_by_name("submit").click()
