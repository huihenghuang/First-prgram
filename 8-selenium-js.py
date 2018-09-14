from selenium import webdriver
import time
chrome = webdriver.Chrome()


chrome.get('https://book.douban.com/')
time.sleep(5)

js = 'document.documentElement.scrollTop=10000'

# chrome.execute_script(js)
chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
input('quit退出：')

chrome.quit()