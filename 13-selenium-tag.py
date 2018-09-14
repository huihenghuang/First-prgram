from selenium import webdriver
import time
chrome = webdriver.Chrome()

chrome.get('https://www.douban.com/')

time.sleep(5)

chrome.find_element_by_class_name('lnk-movie').click()

time.sleep(5)


# 跳转，但是，chrome对应的网页内容依然是跳转之前的网页内容
# chrome.find_element_by_xpath('//div[@class="global-nav-items"]/ul/li[4]').click()
# chrome.find_element_by_xpath('//div[@class="anony-nav-links"]/ul/li[4]').click()

# 浏览器几个窗口
handles = chrome.window_handles

print(handles)

chrome.switch_to.window(handles[1])

time.sleep(5)

# 新页面的标签数据
chrome.find_element_by_xpath('//div[@class="global-nav-items"]/ul/li[4]').click()


time.sleep(10)


chrome.close()