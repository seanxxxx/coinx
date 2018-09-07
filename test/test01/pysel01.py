import selenium
import time
from selenium import webdriver

dr = webdriver.Firefox(executable_path = '/Users/xuanxu/geckodriver')
dr.get('http://baidu.com')
dr.maximize_window()
dr.find_element_by_id('kw').send_keys('图片')
dr.find_element_by_id('su').click()
time.sleep(5)
dr.quit()