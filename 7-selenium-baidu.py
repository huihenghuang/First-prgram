from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get('https://www.baidu.com/')
time.sleep(2)

driver.find_element_by_link_text('设置').click()

time.sleep(2)

driver.find_element_by_link_text('搜索设置').click()

time.sleep(2)

driver.find_element_by_xpath('//option[@value="50"]').click()

time.sleep(2)

driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_id('kw').send_keys('世界杯')

driver.find_element_by_id('su').click()

input('输入任意字母，回车退出：')

driver.quit()