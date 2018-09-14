from selenium import webdriver
import time
chrome = webdriver.Chrome()


url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

chrome.get(url)

time.sleep(2)

chrome.find_element_by_id('email').send_keys('455098435@qq.com')

chrome.find_element_by_id('pwd').send_keys('31415926abc')

verify = input('请输入验证码：')

chrome.find_element_by_id('code').send_keys(verify)

chrome.find_element_by_id('denglu').click()

time.sleep(20)

chrome.quit()