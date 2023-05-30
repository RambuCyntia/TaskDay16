import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self): #test cases 2
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com/")
        driver.find_element(By.ID, "email").send_keys("Task16@sanber.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.NAME, "login-button").click()

if __name__ == '__main__':
    unittest.main()