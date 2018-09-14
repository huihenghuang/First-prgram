from selenium import webdriver
import  time
chrome = webdriver.Chrome()


chrome.get('https://www.douban.com/')
time.sleep(5)

chrome.find_element_by_id('form_email').send_keys('18513106743')

chrome.find_element_by_id('form_password').send_keys('31415926abc')

chrome.find_element_by_class_name('bn-submit').click()

time.sleep(20)

chrome.quit()