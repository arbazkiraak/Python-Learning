from selenium import webdriver
import time

a = raw_input("Enter the Email: \n")
b = raw_input("Enter the password to login : \n")
time.sleep(2)
driver = webdriver.Chrome("C://chromedriver.exe")
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys(a)
driver.find_element_by_name("pass").send_keys(b)
driver.find_element_by_id("loginbutton").click()
