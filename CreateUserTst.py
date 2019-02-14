# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CreateUserTst(unittest.TestCase):
    def setUp(self):
#       self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://192.168.101.240:8443/myportal/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_user_tst(self):
        driver = self.driver
        driver.get("https://192.168.101.240:8443/myportal/login.html")
        driver.maximize_window()
        time.sleep(2.5)
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60040@e-fon.ch")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("123456")
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("60040@e-fon.ch")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("123456")
        driver.find_element_by_name("continue").click()     
        #driver.find_element_by_xpath("//div[@class='col-xs-12']//a").click() #works, open "memberCreateForm"
        #driver.find_element_by_css_selector("div.col-xs-6 > div#organizationUnit_chosen.chosen-container.chosen-container-single.chosen-container-single-nosearch > a.chosen-single > div > b").click() #works, open dropdown menu   
        time.sleep(3.5)
        #driver.quit()
        x = 1
        while x < 3:
            driver.find_element_by_link_text("Create new user").click() #works
            #driver.find_element_by_xpath("//div[@id='organizationUnit_chosen']//b").click() #works, open dropdown menu 
            #time.sleep(1.5)
            #driver.find_element_by_xpath("//div[@class='chosen-drop']/ul/li[5]").click() #works, select and sets required item     
            driver.find_element_by_name("firstName").clear()
            driver.find_element_by_name("firstName").send_keys("F"+str(x))
            time.sleep(0.5)
            driver.find_element_by_name("lastName").clear()
            driver.find_element_by_name("lastName").send_keys("L"+str(x))
            driver.find_element_by_id("loginName").clear()
            time.sleep(0.5)
            driver.find_element_by_id("loginName").send_keys("FL_autotest"+str(x)+"@e-fon.ch")
            time.sleep(1.5)
            driver.find_element_by_id("diffContactEmailChkbox").click()
            time.sleep(1.5)
            driver.find_element_by_id("diffContactEmailChkbox").click()
            time.sleep(1.5)
            #driver.find_element_by_id("voicemailEmailChkbox").click()
            #time.sleep(1.5)
            #driver.find_element_by_id("voicemailEmail").send_keys("FL_voicemailtest"+str(x)+"@e-fon.ch")
            #time.sleep(1.5)
            driver.save_screenshot("./testscreenshots/newUser"+str(x)+".jpg")
            time.sleep(1.5)
            driver.find_element_by_name("saveButton").click()
            time.sleep(1.5)
            driver.find_element_by_css_selector("table#membersTable.table.table-condensed.table-striped.table-medium-font-size.dataTable.no-footer > tbody > tr.odd > td.text-right > a.icon-link > span.icon.table-icon__medium.table-icon__small-highlight.icon-left-spaced").click()
#           driver.find_element_by_css_selector("div.modal-footer > div.row > div.col-xs-12.text-right > button.btn.btn-primary.btn-lg").click() #currently don't work
            time.sleep(1.5)
            driver.find_element_by_xpath("//div[@id='membersTable_wrapper']/table/tbody/tr/td[4]/a[3]/span").click() #delete icon
            time.sleep(1.5)
            driver.find_element_by_css_selector("input#rBtnDeleteYes").click()
            time.sleep(1.5)
            driver.find_element_by_id("rBtnDeleteYes").click()
            time.sleep(0.5)
            driver.find_element_by_css_selector("button#btnMemberDelete.btn.btn-primary.btn-lg").click()
            time.sleep(1.5)
            driver.find_element_by_css_selector("div.modal-footer > button.btn.btn.btn-primary.btn-lg").click() #delete button Yes on confirm.dialog
            time.sleep(0.5)
            driver.find_element_by_id("btnMemberDelete").click()
            time.sleep(0.5)
            x += 1
            print x
            driver.back()
            driver.implicitly_wait(300)
            #continue
        driver.find_element_by_link_text(u"⚡Logout").click()
    
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
