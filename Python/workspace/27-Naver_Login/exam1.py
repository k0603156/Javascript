import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome('data/chromedriver.exe')
driver.implicitly_wait(10)

driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(3)

#myid = 'test'   
#mypw = '1234'   

script = "document.getElementById('id').value='%s'" %myid
driver.execute_script(script)

script = "document.getElementById('pw').value='%s'" %mypw
driver.execute_script(script)

btn = driver.find_element_by_css_selector('.btn_global');
btn.click()
time.sleep(3)

driver.get('https://mail.naver.com/')
time.sleep(3)

soup = bs(driver.page_source, 'html.parser')

mail_title = soup.select('.mail_title')

title_list = []
for v in mail_title :
    title_list.append(v.text.strip())

print(title_list)

















