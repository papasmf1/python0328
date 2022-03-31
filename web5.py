# web5.py 

from selenium import webdriver

driver = webdriver.Chrome('c:\\work\\chromedriver')

driver.implicitly_wait(3)
driver.get('https://google.com')

# driver.get('https://nid.naver.com/nidlogin.login')
# driver.find_element_by_name('id').send_keys('kim')


# driver.find_element_by_name('pw').send_keys('1234')