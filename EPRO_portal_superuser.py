# -*- coding: utf-8 -*-
#from operator import div
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, MySQLdb
#import os

class EPROPortalSuperuser(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
#       self.driver = webdriver.Firefox()
#       dir = os.path.dirname(__file__)
#       ie_driver_path = dir + "\IEDriverServer.exe"
#       ie_driver_path = "C:\Python27\IEDriverServer.exe"
#       self.driver = webdriver.Ie('C:\Python27\IEDriverServer.exe') #create a new Internet Explorer session
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.102.162:9090/portal/login#/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    db = MySQLdb.connect(host="192.168.102.162",
                     user="root",
                     passwd="root",
                     db="webadmin_20180130")
    
#   db = MySQLdb.connect(host="192.168.101.240",
#                       user="root",
#                       passwd="root",
#                       db="webadmin_20160105")

    cur = db.cursor() #You must create a Cursor object to execute all the queries which you need
    cur.execute("SELECT * FROM login WHERE email='60040@e-fon.ch';")
    for row in cur.fetchall():
        login_id = row[0]
        print ('login_id:', login_id, row[3], 'md5password:', row[4])
    db.close()
    
    def test_e_p_r_o_portal_superuser(self):
        driver = self.driver
        driver.maximize_window()
        time.sleep(0.5)
        driver.get("http://192.168.102.162:9090/portal/")
        time.sleep(0.5)
        driver.find_element_by_id("j_username").clear()
        driver.find_element_by_id("j_username").send_keys("60040@e-fon.ch")
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("123456")
        time.sleep(1.5)
        driver.find_element_by_xpath("//login-form/div/div/div[2]/div/form/div[3]/div/button").click() #works
#       driver.find_element_by_id("j_username").clear()
#       driver.find_element_by_id("j_username").send_keys("60040@e-fon.ch")
#       driver.find_element_by_id("j_password").clear()
#       driver.find_element_by_id("j_password").send_keys("123456")
#       driver.find_element_by_name("continue").click()
        time.sleep(1.5)
#       driver.find_element_by_css_selector("login-form > div > div > div.widget.login-window > div > form > div:nth-child(3) > div > button.btn.btn-default.btn-lg").click()   #works
#       driver.find_element_by_css_selector("body > login-app > div > login-form > div > div > div.widget.login-window > div > form > div:nth-child(3) > div > button").click() #don't works
        time.sleep(1.5)
        driver.find_element_by_link_text("User").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Numbers").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Abbreviated dialling").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Manage abbreviated numbers").click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("xxxxx")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("xxxxx")
        driver.find_element_by_xpath("(//input[@type='text'])").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        time.sleep(1.5)
#       driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("xxxxxxx")     
        driver.find_element_by_xpath("//input[@type='text']").send_keys("2345")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("2345")
        time.sleep(1.5)
#       driver.find_element_by_xpath("//form[@class='form-horizontal submit ng-untouched ng-pristine ng-valid']/div[2]/button").click() #also works
        driver.find_element_by_css_selector("body > my-app > ng-component > div > div:nth-child(2) > div > tabs > ng-component > div > div > div > div:nth-child(5) > div > section > form > div.col-xs-4.text-right > button").click() #works
        time.sleep(2.5)
        driver.find_element_by_link_text("Abbreviated numbers").click()
        time.sleep(2.5)
        driver.find_element_by_xpath("//section[@class='form-section form-section__borderless']/div/div/div/div/div/input").clear()
        driver.find_element_by_xpath("//section[@class='form-section form-section__borderless']/div/div/div/div/div/input").send_keys("2345")        
#       driver.find_element_by_css_selector("body > my-app > ng-component > div > div:nth-child(2) > div > tabs > ng-component > div > div > div:nth-child(2) > div > efon-table > section > ng-table > table > tbody > tr > td.nowrap.alignRight > a:nth-child(1) > span").click() #works
        driver.find_element_by_xpath("//body/my-app/ng-component/div/div[2]/div/tabs/ng-component/div/div/div[2]/div/efon-table/section/ng-table/table/tbody/tr/td[5]/a[1]/span").click()   #works
        time.sleep(2.5)
        driver.find_element_by_xpath("//body/my-app/modal-placeholder/ng-component/system-modal-template/div/div/div/div[3]/button[1]").click() #works
#       driver.find_element_by_xpath("//confirmation-modal//button[text()='Yes']").click() # Alternative way simply get the button (or other objects) using the text property
        time.sleep(1.5)
#       driver.find_element_by_link_text("Provisioning").click()
#       driver.find_element_by_link_text("Hunt Groups").click()
#       driver.find_element_by_xpath("//ul[@class='list-inline sub-navigation']/li[2]/a").click()
#       driver.find_element_by_xpath("//ul[@class='list-inline sub-navigation']/li[3]/a").click()
#       driver.find_element_by_xpath("//ul[@class='list-inline sub-navigation']/li/a").click()
#       time.sleep(0.5)
#       driver.find_element_by_link_text("End devices").click()
#       driver.find_element_by_link_text("Call forwarding").click()   
#       driver.find_element_by_link_text("Last calls").click()
#       driver.find_element_by_link_text("Subscriptions").click()
#       driver.find_element_by_link_text("Bills").click()
#       driver.find_element_by_link_text("IVRs").click()
#       driver.find_element_by_link_text("Call pick-ups").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Organisation").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Contact data").click()
        time.sleep(1.5)
#       driver.find_element_by_xpath("//ul[@id='mainNavbar']/li[12]/a").click() #works
        driver.find_element_by_link_text("Language").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Access").click()
        time.sleep(1.5)
        driver.save_screenshot('./testscreenshots/contact-data_access_before.jpg') #before data change
        time.sleep(1.5)
        driver.find_element_by_xpath("//form/div/div[2]/a/span").click()
        time.sleep(1.5)
        driver.find_element_by_name("email").clear()
        time.sleep(0.5)
        driver.find_element_by_name("email").send_keys("60040@e-fon.ch")
        time.sleep(0.5)
        driver.find_element_by_link_text("Cancel").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//form/div/div[2]/a/span").click()
        time.sleep(0.5)
        driver.find_element_by_name("email").clear()
        time.sleep(1.5)
        driver.find_element_by_name("email").send_keys("600040@e-fon.ch")
        time.sleep(1.5)
        #loginNameForm > div:nth-child(2) > div > a.btn.btn-primary.btn-lg
        #driver.find_element_by_css_selector("contact-access-login > section > form > div[2] > a.btn.btn-primary.btn-lg").click()
        driver.find_element_by_css_selector("#loginNameForm > div:nth-child(2) > div > a.btn.btn-primary.btn-lg").click()
        #driver.find_element_by_xpath("//form[@id='loginNameForm']/div[2]/div/a").click()
        #driver.find_element_by_link_text("Save").click()
        time.sleep(1.5)
        driver.quit()
#       driver.find_element_by_xpath("//section[2]/form/div/div[2]/a/span").click()
#       driver.find_element_by_link_text("Cancel").click()
#       driver.find_element_by_xpath("//section[2]/form/div/div[2]/a/span").click()
#       driver.find_element_by_xpath("//section[2]/form[2]/div[1]/div/input").send_keys("123456")
#       driver.find_element_by_xpath("//section[2]/form[2]/div[2]/div/input").send_keys("12345Asdf!")
#       driver.find_element_by_xpath("//section[2]/form[2]/div[3]/div/input").send_keys("12345Asdf!")
#       driver.find_element_by_link_text("Save").click()     
#       driver.find_element_by_xpath("//customer-header/div[2]/div[2]/div[1]/div[2]/a").click() #logout for updated loginname - does not work
#       driver.get("http://192.168.102.162:9090/portal/")
#       time.sleep(0.5)        
#       driver.find_element_by_id("j_username").clear()
#       driver.find_element_by_id("j_username").send_keys("600040@e-fon.ch")        
#       driver.find_element_by_id("j_password").clear()
#       driver.find_element_by_id("j_password").send_keys("123456")
#       time.sleep(1.5)
#       driver.find_element_by_xpath("//login-form/div/div/div[2]/div/form/div[3]/div/button").click() #works     
        time.sleep(1.5)
        driver.find_element_by_link_text("Contact data").click()
        time.sleep(1.5)
        driver.find_element_by_link_text("Access").click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//form/div/div[2]/a/span").click()
        time.sleep(0.5)
        driver.find_element_by_name("email").clear()
        time.sleep(0.5)
        driver.find_element_by_name("email").send_keys("60040@e-fon.ch")
        time.sleep(1.5)
        driver.find_element_by_link_text("Save").click()
        time.sleep(1.5)
#       //form[contains(@class,'ng-untouched')]/div[2]/div/label # Use of contains() to match against a partial value. I've found this to be useful when working against angular
#       driver.find_element_by_xpath("//p[@id, 'one']/following-sibling::p") # More one solution
#       driver.find_element_by_xpath("//calendar-server-settings//a[@name='editLink']").click()
#       time.sleep(1.5)
#       driver.find_element_by_link_text("Cancel").click()
#       time.sleep(1.5)
#       driver.find_element_by_xpath("//calendar-server-settings//a[@name='editLink']").click()
#       time.sleep(0.5)
#       driver.find_element_by_xpath("//calendar-server-settings/section/form/div[2]/div/input").clear()
#       time.sleep(0.5)
#       driver.find_element_by_xpath("//calendar-server-settings/section/form/div[2]/div/input").send_keys("Test_name")
#       time.sleep(0.5)
#       driver.find_element_by_xpath("//form[@id='calendarServerSettingsForm']/div[3]/div/input[@name='port']").clear()
#       time.sleep(0.5)
#       driver.find_element_by_xpath("//form[@id='calendarServerSettingsForm']/div[3]/div/input[@name='port']").send_keys("0")
#       time.sleep(0.5)
#       driver.find_element_by_xpath("//form[@id='calendarServerSettingsForm']/div[5]/div/input[@name='userName']").clear()
#       time.sleep(0.5)
#       driver.find_element_by_xpath("//form[@id='calendarServerSettingsForm']/div[5]/div/input[@name='userName']").send_keys("Tst_username")
#       time.sleep(0.5)
#       driver.find_element_by_xpath("//form[@id='calendarServerSettingsForm']/div[8]/div/input[@name='mailbox']").clear()
#       time.sleep(0.5)
#       driver.find_element_by_xpath("//form[@id='calendarServerSettingsForm']/div[8]/div/input[@name='mailbox']").send_keys("Test@test.com")            
#       time.sleep(0.5)        
#       driver.find_element_by_link_text("Save").click()
#       time.sleep(1.5)
        driver.find_element_by_xpath("//ip-restriction//a[@name='editLink']").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("+ Add new IP address").click()
        time.sleep(0.5)
        driver.find_element_by_name("newIp").clear()
        time.sleep(0.5)
        driver.find_element_by_name("newIp").send_keys("127.0.0.1")
        time.sleep(0.5)
        driver.find_element_by_link_text("Cancel").click()        
#       driver.find_element_by_link_text("Save").click()
        time.sleep(0.5)
        db = MySQLdb.connect(host="192.168.102.162",
                                 user="root",
                                 passwd="root",
                                 db="webadmin_20180130")
        
 #      db = MySQLdb.connect(host="192.168.101.240",
 #                          user="root",
 #                          passwd="root",
 #                          db="webadmin_20160105")

 #      cursor = db.cursor()
 #      sql="UPDATE login SET md5password='7aad9504c5e209be607a70566b04df4009d3f141' WHERE email='60040@e-fon.ch' " #works
        sql="UPDATE login SET md5password=(%s) WHERE login_id=login_id"
        k='7aad9504c5e209be607a70566b04df4009d3f141'
        cursor = db.cursor() #You must create a Cursor object to execute all the queries which you need  
        try:
              cursor.execute(sql, (k,))
              #cursor.execute(sql)
              db.commit()
        except:
              db.rollback()
        db.close()
        driver.save_screenshot('./testscreenshots/contact-data.jpg') #after data change
        time.sleep(1.5)
#       driver.find_element_by_xpath("//a[contains(@href, 'logout')]").click()
#       driver.find_element_by_css_selector("body.dashboard > div.container-non-responsive-header > div.row.header.display_table > customer-header > div.col-md-6.table_cell-align.alignRight_important > div.col-md-8 > div.row.text-center > div.col-md-4.text-center > a.btn.btn-default.btn-lg.header-logout_button.text-center").click() #works
        driver.find_element_by_css_selector("a.btn.btn-default.btn-lg.header-logout_button.text-center").click()
#       driver.find_element_by_xpath("//body/div/div/customer-header/div[2]/div[2]/div[1]/div[2]/a").click()
#       driver.find_element_by_link_text(u"⚡Logout").click()
    
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