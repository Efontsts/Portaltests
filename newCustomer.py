from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class NewCustomer(unittest.TestCase):
    def setUp(self):
#       self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://change-this-to-the-site-you-are-testing/"
        self.verificationErrors = []
    
    def test_new_customer(self):
        driver = self.driver
        driver.get("https://192.168.101.240:8443/portal/login.html")
        driver.maximize_window()
        driver.find_element_by_name("j_username").clear()
        driver.find_element_by_name("j_username").send_keys("ihoradmin@e-fon.ch")
        driver.find_element_by_name("j_password").clear()
        driver.find_element_by_name("j_password").send_keys("123456")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_name("j_username").clear()
        driver.find_element_by_name("j_username").send_keys("ihoradmin@e-fon.ch")
        driver.find_element_by_name("j_password").clear()
        driver.find_element_by_name("j_password").send_keys("123456")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_link_text("New customer").click()
        driver.find_element_by_name("resellerCustomerId").clear()
        driver.find_element_by_name("resellerCustomerId").send_keys("123456789012345")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("123456789012347@e-fon.ch")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("Inttest")
        driver.find_element_by_name("lastName").clear()
        driver.find_element_by_name("lastName").send_keys("Ln")
        driver.find_element_by_name("firstName").clear()
        driver.find_element_by_name("firstName").send_keys("Fn")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("12345Asdf!")        
        driver.find_element_by_name("address1").clear()
        driver.find_element_by_name("address1").send_keys("Baden")
        driver.find_element_by_name("zipCode").clear()
        driver.find_element_by_name("zipCode").send_keys("5400")
        time.sleep(0.5)
        driver.find_element_by_id("ext-gen12").click()
        time.sleep(0.5)        
        driver.find_element_by_xpath("//div[@id='ext-gen14']/div[5]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//select[@id='citySelect']/option[2]").click()
        time.sleep(2.5)
        #driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
