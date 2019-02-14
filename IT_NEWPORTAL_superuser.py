# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ITNEWPORTALSuperuser(unittest.TestCase):
    def setUp(self):
#       self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://192.168.101.240:8443/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_i_t_n_e_w_p_o_r_t_a_l_superuser(self):
        driver = self.driver
        driver.get("https://192.168.101.240:8443/myportal/login.html")
        driver.maximize_window()
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60040@e-fon.ch")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("123456")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60040@e-fon.ch")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("123456")        
        driver.find_element_by_name("continue").click()
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Contact data").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Language").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/a/div/b").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/div/ul/li[text()='Italiano']").click()
        time.sleep(0.5)        
        driver.find_element_by_link_text("Utenti").click()
        time.sleep(1.5)
#       driver.find_element_by_xpath("//table[@id='membersTable']/tbody/tr/td[4]/a[2]/span").click()
#       driver.find_element_by_link_text("Assegnazioni").click()
#       driver.find_element_by_link_text("Trasferimenti di chiamata").click()
#       driver.find_element_by_link_text("Voicemail").click()
#       driver.find_element_by_link_text("Messaggi fax").click()
#       driver.find_element_by_link_text("Terminali").click()
#       driver.find_element_by_link_text("Sicurezza").click()
#       driver.find_element_by_link_text("Messaggi di benvenuto").click()
#       driver.find_element_by_css_selector("button.close").click()
        driver.find_element_by_link_text("Numeri").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Numeri di cellulare").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Chiamate circolare").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Provisioning").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Modelli di telefono").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Gestore del provisioning").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Fatture").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Abbonamenti").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Inoltro chiamate").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Terminali").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Ultime chiamate").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("IVR").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Selezione rapida").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Gestione numeri di selezione rapida").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Risposta a una chiamata").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Gestione file").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Music On Hold").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Estensioni manuali").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Code chiamate").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Stato").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Registrazioni").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Report").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(1.5)
        #driver.find_element_by_link_text("Organizzazione").click()
        #driver.find_element_by_link_text("Elenco utenti").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Dadi di contatto").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Contatto").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Lingua").click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/a/div/b").click()
        time.sleep(2.5)
        driver.find_element_by_xpath("//body/div[4]/div[2]/div/section/form/div/div/div/div/ul/li[text()='English']").click()
        time.sleep(2.5)        
        driver.find_element_by_link_text(u"⚡Logout").click()
        #driver.quit()
    
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
