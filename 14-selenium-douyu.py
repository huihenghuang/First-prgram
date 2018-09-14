from selenium import webdriver
import time

chrome = webdriver.Chrome()



# invalid selector xpath语句错误
# 标题
# titles = chrome.find_elements_by_xpath('//h3[@class="ellipsis"]')
#
# # 关注量
# counts = chrome.find_elements_by_xpath('//span[@class="dy-num fr"]')
#
# print(titles)
# print(counts)
#
# print(len(titles),len(counts))
#
# for title in titles:
#     print(title.text)

fp = open('./斗鱼.txt',mode='a',encoding='utf-8')

# 第一页内容
chrome.get('https://www.douyu.com/directory/all')
time.sleep(2)
# 将弹出来的对话框关闭
try:
    chrome.find_element_by_class_name('pop-zoom-hide').click()
except Exception as e:
    pass

while True:

    titles = chrome.find_elements_by_xpath('//h3[@class="ellipsis"]')
    counts = chrome.find_elements_by_xpath('//span[@class="dy-num fr"]')

    for title,count in zip(titles[10:],counts):
        fp.write(title.text.strip()+count.text.strip()+'\n')

#     给一个退出的条件
#     <a href="#" class="shark-pager-next shark-pager-disable shark-pager-disable-next">下一页</a>
#     <a href="#" class="shark-pager-prev shark-pager-disable shark-pager-disable-prev">上一页</a>
    index = chrome.page_source.find('shark-pager-disable-next')

    if index !=-1:
        break

#     点击下一页
    chrome.find_element_by_class_name('shark-pager-next').click()
    time.sleep(5)
