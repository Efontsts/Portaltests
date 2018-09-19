# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UserInNewPortal(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        #self.driver = webdriver.Ie("C://Python27//IEDriverServer.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://192.168.101.240:8443/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_user_in_new_portal(self):
        driver = self.driver
        driver.get("https://192.168.101.240:8443/myportal/login.html")
        time.sleep(1.5) # Let the page load
        driver.maximize_window()
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60050@e-fon.ch")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("123456")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60050@e-fon.ch")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("123456")
        driver.find_element_by_name("continue").click()
        time.sleep(1.5)
        driver.find_element_by_id("buttonAllCalls").click()
        time.sleep(1.5)
        driver.find_element_by_id("buttonMissedCalls").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Show all calls").click()
        time.sleep(0.5)
        driver.find_element_by_id("buttonIncomingCalls").click()
        time.sleep(0.5)
        driver.find_element_by_id("buttonOutgoingCalls").click()
        time.sleep(0.5)
        driver.find_element_by_id("buttonOutgoingByMonthCalls").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Overview").click()
        time.sleep(0.5)
        driver.get('https://192.168.101.240:8443/myportal/user/dashboard.html')
        time.sleep(0.5)
        driver.save_screenshot('./testscreenshots/memberOverview.jpg')
        time.sleep(0.5)
        driver.find_element_by_link_text("Fax arrived").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Fax settings").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Call forwarding").click()
        time.sleep(0.5)
        driver.find_element_by_name("delay1").clear()
        time.sleep(0.5)
        driver.find_element_by_name("delay1").send_keys("10")
        time.sleep(0.5)
        driver.find_element_by_name("save").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Voicemail").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Voicemail settings").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Announcements").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Send text message").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Manage sender numbers/names").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Hunt groups").click()
        time.sleep(0.5)
        #driver.find_element_by_css_selector("a.nav-dropdownp-link > span.icon").click()
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Queues").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Configure").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Status").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Recordings").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Queues as agent").click()
        time.sleep(0.5)      
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        #driver.find_element_by_link_text("Send Fax").click()
        #driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Contact data").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Language").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Access").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Contact").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("End devices").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Abbreviated dialling").click()
        time.sleep(1.5)
        driver.quit()
        #driver.find_element_by_link_text(u"⚡Log out").click()
    
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
 
    def check_exists_by_xpath(xpath):
        try:
            webdriver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
