from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get('https://www.baidu.com/')
time.sleep(5)


# driver.save_screenshot('./baidu.png')
#
# driver.quit()

# 文本输入框了
driver.find_element_by_id('kw').send_keys('美女')


# 进行搜索
driver.find_element_by_id('su').click()

time.sleep(5)

driver.back()

time.sleep(5)

driver.forward()

input('任意键退出：')
driver.quit()