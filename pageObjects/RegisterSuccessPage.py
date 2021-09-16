class RegisterSuccessPage():
  def __init__(self, driver):
    self.driver = driver


  def back_to_register(self):
    return self.driver.find_element_by_css_selector("[href='register.php']")
        