from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C://chromedriver.exe")
browser.get("https://yahoo.com")
assert 'Yahoo' in browser.title

element = browser.find_element_by_name('p')
raw_input("what you want to Search ?\n")
element.send_keys('hackerone'+ Keys.RETURN)
raw_input("Enter to Proceed")
browser.quit()
