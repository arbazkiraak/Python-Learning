from selenium import webdriver
import time

driver = webdriver.Chrome("C://chromedriver.exe") #For Windows
#driver = webdriver.Firefox() #For Linux :P
a = raw_input("Enter the Name of list : \n")
b = open(a,"r").readlines()
for line in b:
    line = line.rstrip("\n")
    line = line.rstrip("\r")
    print line
    print "\n"* 2
    driver.get(line)
    time.sleep(3)

