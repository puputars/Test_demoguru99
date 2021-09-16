import pytest
from selenium import webdriver
import time
driver = None

@pytest.fixture(scope="class")
def setup(request):
    global driver

    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    driver.get("http://demo.guru99.com/test/newtours/register.php")
    driver.maximize_window()
    request.cls.driver = driver
    #yield
    #driver.close()