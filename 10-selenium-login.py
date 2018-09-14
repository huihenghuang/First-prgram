from selenium import webdriver
import time
driver = webdriver.Chrome()


url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes'

driver.get(url=url)

time.sleep(5)

driver.find_element_by_name('username').send_keys('18513106743')

driver.find_element_by_name('password').send_keys('31415926abc')

# 登陆
driver.find_element_by_name('loginsubmit').click()

time.sleep(10)

driver.save_screenshot('./chinaUnix.jpg')

driver.quit()