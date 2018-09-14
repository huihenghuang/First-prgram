# web驱动
from selenium import webdriver

import time

chrome = webdriver.Chrome()

chrome.get(url='https://sou.zhaopin.com/?jl=765&jt=&kw=Python&kt=3')

time.sleep(5)


html = chrome.page_source

print(html)

input('点击回车退出程序：')

chrome.quit()