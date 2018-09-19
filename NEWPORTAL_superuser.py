
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NEWPORTALSuperuser(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        self.driver.implicitly_wait(30)    
        self.base_url = "https://192.168.101.240:8443/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_n_e_w_p_o_r_t_a_l_superuser(self):
        driver = self.driver
        driver.get("https://192.168.101.240:8443/myportal/login.html")
        time.sleep(1.5) # Let the page load
        #driver.set_window_size(1024, 600)
        driver.maximize_window()        
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60040@e-fon.ch")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("123456")
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60040@e-fon.ch")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_id("searchInput").clear()
        driver.find_element_by_id("searchInput").send_keys("sven")
        time.sleep(0.5)
        driver.find_element_by_xpath("//table[@id='membersTable']//tbody/tr[1]/td[4]/a[3]/span").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Allocations").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Forwarding").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Voicemail").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Faxes").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("End devices").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Security").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Announcements").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("button.close").click()
        driver.save_screenshot('./testscreenshots/memberOverview.jpg')
        time.sleep(0.5)    
        #driver.quit()        
        driver.find_element_by_link_text("Numbers").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Mobile numbers").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Hunt groups").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Provisioning").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Phone models").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Provisioning manager").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Bills").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Call forwarding").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("End devices").click()
        #time.sleep(1.5)
        driver.find_element_by_link_text("Last calls").click()
        time.sleep(0.5)
        driver.find_element_by_id("buttonIncomingCalls").click()
        time.sleep(0.5)
        driver.find_element_by_id("buttonOutgoingCalls").click()
        time.sleep(0.5)
        driver.find_element_by_id("buttonOutgoingByMonthCalls").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("IVRs").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Abbreviated dialling").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Manage abbreviated numbers").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//div[@id='navbar-collapse']//a/span").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Call pick-ups").click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//div[@class='collapse navbar-collapse']//a/span").click()
        #driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("File management").click()
        time.sleep(1.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Music On Hold").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Conference calls").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()        
        time.sleep(0.5)
        driver.find_element_by_link_text("Manual extensions").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Queues").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Status").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Recordings").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1.5)       
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(1.5)
#       driver.find_element_by_link_text("Organisation").click()
#       driver.find_element_by_link_text("User overview").click()     
#       driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        driver.find_element_by_link_text("Recorded calls configuration").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Configuration").click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//input[@id='upload']").click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//body/div[4]/div[3]/div/div[3]/div/div[5]/div/button[2]").click()
#       driver.find_element_by_xpath("//body/div[5]/div/div/div[3]/button[1]").click()
        time.sleep(1.5)
        driver.find_element_by_css_selector("li.flexMenu-viewMore > a > span.icon").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Contact data").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Contact").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Language").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Access").click()
        time.sleep(1.5)      
        driver.find_element_by_xpath("//div[@class='text-center col-xs-4']//a").click() #Logout
        #driver.find_element_by_link_text(u"⚡Logout").click()
    
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
