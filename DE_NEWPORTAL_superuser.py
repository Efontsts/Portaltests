# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class DENEWPORTALSuperuser(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        self.driver.implicitly_wait(30)    
        self.base_url = "https://192.168.101.240:8443/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_d_e_n_e_w_p_o_r_t_a_l_superuser(self):
        driver = self.driver
        driver.get("https://192.168.101.240:8443/myportal/login.html")
        driver.maximize_window()
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60040@e-fon.ch")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("123456")
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60040@e-fon.ch")
        driver.find_element_by_name("continue").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Contact data").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Language").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/a/div/b").click()
        time.sleep(0.5)
#       driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/div/ul/li[2]").click() # works
        driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/div/ul/li[text()='Deutsch']").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Benutzer").click()
        time.sleep(0.5)
#       driver.find_element_by_link_text("Voicemail").click()
#       driver.find_element_by_link_text("Fax Nachrichten").click()
#       driver.find_element_by_link_text(u"Endgeräte").click()
        driver.find_element_by_link_text("Nummern").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Mobilnummern").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Ringrufe").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Provisionierung").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Telefonmodelle").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Provisionierungsmanager").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Rechnungen").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Abos").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Rufumleitungen").click()
        time.sleep(0.5)
#       driver.find_element_by_link_text(u"Gespräche").click()
#       driver.find_element_by_id("buttonIncomingCalls").click()
#       driver.find_element_by_id("buttonOutgoingCalls").click()
#       driver.find_element_by_id("buttonOutgoingByMonthCalls").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("IVRs").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Kurzwahlen").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Kurzwahlnummern verwalten").click()
        time.sleep(0.5)
#       driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
#       driver.find_element_by_link_text(u"Rufübernahmen").click()
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Dateiverwaltung").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Music On Hold").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Manuelle Extensions").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Warteschlangen").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Status").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Aufnahmen").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Berichte").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Kontaktdaten").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Zugriff").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Kontakt").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Sprache").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/a/div/b").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/div/ul/li[text()='English']").click()
        time.sleep(0.5)
        driver.find_element_by_link_text(u"⚡Logout").click()
    
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
    
