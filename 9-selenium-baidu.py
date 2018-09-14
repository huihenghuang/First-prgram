from selenium import webdriver
import time
chrome = webdriver.Chrome()


chrome.get('https://www.baidu.com/')
time.sleep(5)

img = chrome.find_element_by_class_name('index-logo-src')

chrome.execute_script("$(arguments[0]).fadeOut()",img)

chrome.execute_script('var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\"')

input('输入任意，回车退出')

chrome.quit()