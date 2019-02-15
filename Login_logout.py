from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class LoginLogout(unittest.TestCase):
    def setUp(self):
#       self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://192.168.101.240:8443/portal/"
        self.verificationErrors = []
    
    def test_login_logout(self):
        driver = self.driver
        driver.get("https://192.168.101.240:8443/portal/login.html")
        driver.maximize_window()
#       driver.find_element_by_link_text("Login").click()
        driver.find_element_by_name("j_username").clear()
        driver.find_element_by_name("j_username").send_keys("ihoradmin@e-fon.ch")
        driver.find_element_by_name("j_password").clear()
        driver.find_element_by_name("j_password").send_keys("123456")
        driver.find_element_by_name("continue").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_name("j_username").clear()
        driver.find_element_by_name("j_username").send_keys("ihoradmin@e-fon.ch")
        driver.find_element_by_name("j_password").clear()
        driver.find_element_by_name("j_password").send_keys("123456")
        driver.find_element_by_name("continue").click()
        textsave = open("textsave.txt","w")
        driver.find_element_by_id("ext-gen43").click()
        driver.find_element_by_xpath("(//img[@title='Act on behalf of this customer'])[2]").click()    
        time.sleep(1.5) # Let the page load
        x = 1           
        while x <= 3:
            driver.find_element_by_link_text("User overview").click()
            #driver.find_element_by_xpath("//input[@value='Create user']").click()
            driver.find_element_by_css_selector("tr.topAlignedRow > td > table > tbody > tr.topAlignedRow > td > table > tbody > tr > td > input.button").click()
            driver.find_element_by_name("firstName").clear()
            driver.find_element_by_name("firstName").send_keys("F"+str(x))
            driver.find_element_by_name("lastName").clear()
            driver.find_element_by_name("lastName").send_keys("L"+str(x))
            time.sleep(0.5)
            driver.find_element_by_css_selector("body > table > tbody > tr.topAlignedRow > td > table > tbody > tr:nth-child(7) > td:nth-child(3) > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input").click()
            time.sleep(0.5)
            driver.find_element_by_css_selector("body > table > tbody > tr.topAlignedRow > td > table > tbody > tr:nth-child(7) > td:nth-child(3) > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input").send_keys("FLtest"+str(x)+"@e-fon.ch")
            #driver.find_element_by_id("diffContactEmailChkbox").send_keys("FLtest"+str(x)+"@e-fon.ch")
            time.sleep(0.5)
            #driver.find_element_by_id("voicemailEmailChkbox").click()
            #driver.find_element_by_id("voicemailEmail").clear()
            #driver.find_element_by_id("voicemailEmail").send_keys("FLtest"+str(x)+"@e-fon.ch")
            textsave.write("Iteration "+str(x)+"_Ok\n")
            time.sleep(1.5)
            driver.save_screenshot("./testscreenshots/UserConfigOverview "+str(x)+".jpg")
            #driver.find_element_by_xpath("//body/table/tbody/tr[2]/td/table/tbody/tr[7]/td[3]/form/table/tbody/tr[21]/td[2]/input").click() #works
            driver.find_element_by_xpath("//input[@value='Create']").click()
            time.sleep(0.5)
            driver.find_element_by_css_selector("img[title=\"Delete user\"]").click()
            time.sleep(0.5)
            driver.find_element_by_id("rBtnDeleteYes").click()
            #driver.find_element_by_id("btnMemberDelete").click() #works
            driver.find_element_by_css_selector("input#btnMemberDelete.button").click() #works
            #driver.find_element_by_css_selector("input.button").click() #works
            driver.find_element_by_css_selector("tr.topAlignedRow > td > table > tbody > tr.topAlignedRow > td > table > tbody > tr > td > input.button").click() #works
            time.sleep(0.5)
            x += 1
            print x
            driver.back()
        driver.implicitly_wait(30)
        textsave.close()
        driver.find_element_by_link_text("Logout").click()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
