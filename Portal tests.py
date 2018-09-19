# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, MySQLdb
#import os
import Login_logout
import userInNewPortal
import NEWPORTAL_superuser
import EPRO_portal_superuser

def optionselect():

            print "Available tests:\n1 Create user in old portal\n2 Check member in myportal\n3 Check myportal\n4 Check EPRO portal"
            i = int(raw_input("Select needed test: "))

	    if i == 1:

		print "1 Create userin old portal"
		unittest.main (module = Login_logout)

	    elif i == 2:

		print "2 Check member in myportal"
		unittest.main (module = userInNewPortal)

	    elif i == 3:

		print "3 Check myportal"
		unittest.main (module = NEWPORTAL_superuser)
			
	    elif i == 4:

		print "4 Check EPRO portal"
		unittest.main (module = EPRO_portal_superuser)			
			
	    else:

		print "Available tests:\n1 Create userin old portal\n2 Create user in myportal\n3 Check myportal\n4 Check EPRO portal"

optionselect()

