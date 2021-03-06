# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class DE_EPROPortalSuperuser(unittest.TestCase):
    def setUp(self):
#       self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.102.162:9090/portal/login#/"
        self.verificationErrors = []
        self.accept_next_alert = True 
    
    def test_d_e_e_p_r_o_portal_superuser(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://192.168.102.162:9090/portal/")
        time.sleep(0.5)
        driver.find_element_by_id("j_username").clear()
        driver.find_element_by_id("j_username").send_keys("60040@e-fon.ch")
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("123456")
        driver.find_element_by_id("j_username").clear()
        driver.find_element_by_id("j_username").send_keys("60040@e-fon.ch")
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("123456")
        time.sleep(1.5)
        driver.find_element_by_name("continue").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("User").click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//ul[@id='mainNavbar']/li[9]/a").click()
        #driver.find_element_by_link_text("Contact data").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Language").click()       
        time.sleep(1.5)
        #driver.find_element_by_css_selector("body > my-app > ng-component > div > div:nth-child(2) > div > tabs > contact-language > div > div > section > div > div > div > select").click()
        #time.sleep(1.5)
        #driver.find_element_by_name("locale").select_by_visible_text("Deutsch").click()
        driver.find_element_by_css_selector("contact-language > div > div > section > div > div > div > select > option:nth-child(1)").click()
        time.sleep(1.5)        
        #driver.find_element_by_link_text("Numbers").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text(":::Mobile Numbers").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text(":::Mobile Routings").click()
        #time.sleep(1.5)        
        #driver.find_element_by_link_text(":::Organisation").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text(u"Benutzerübersicht").click()
        #time.sleep(0.5)
        #driver.find_element_by_link_text("Recorded calls").click()
        #time.sleep(0.5)
        #driver.find_element_by_link_text("Konfiguration").click()
        #time.sleep(0.5)
        driver.find_element_by_link_text(":::Abbreviated dialling").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Kurzwahlnummern verwalten").click()
        time.sleep(1.5)
        driver.find_element_by_link_text(":::Call pick-ups").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Hunt Groups").click()
        time.sleep(1.5)
        driver.find_element_by_link_text(":::Contact data").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Sprache").click()       
        time.sleep(1.5)
        #driver.find_element_by_css_selector("body > my-app > ng-component > div > div:nth-child(2) > div > tabs > contact-language > div > div > section > div > div > div > select").click()
        driver.find_element_by_css_selector("contact-language > div > div > section > div > div > div > select > option:nth-child(3)").click()
        time.sleep(1.5)                
        #driver.find_element_by_link_text(":::Contact data").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text("Zugriff").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text("End devices").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text("Bills").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text("Provisioning").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text("Telefonmodelle").click()
        #time.sleep(1.5)
        #driver.find_element_by_link_text("Provisionierungsmanager").click()
        #time.sleep(1.5)
        driver.find_element_by_link_text("IVRs").click()
        time.sleep(1.5)
        driver.find_element_by_css_selector("body > div > div > customer-header > div.col-md-8.table_cell-align.alignRight_important > div.col-md-8 > div.row.text-center > div.col-md-4.text-center > form > button > span:nth-child(2)").click()
        #driver.find_element_by_xpath("//a[contains(@href,'logout')]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
