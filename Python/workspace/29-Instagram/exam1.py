from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
import time
import datetime as dt
import os
import requests

options = webdriver.ChromeOptions()
mobile_emulation = {'deviceName': 'Nexus 5'}
options.add_experimental_option('mobileEmulation', mobile_emulation)

driver = webdriver.Chrome('data/chromedriver.exe', options=options)
driver.implicitly_wait(10)

driver.get('https://www.instagram.com/accounts/login/')

#myid = 'test'
#mypw = '123456'

try :
    username = WebDriverWait(driver, 10)\
        .until(lambda drv: drv.find_element_by_css_selector("input[name='username']"))
    username.send_keys(myid)
except Exception as ex:
    print('아이디 입력 실패 >> ', ex)
    quit()

try :
    password = WebDriverWait(driver, 10)\
        .until(lambda drv: drv.find_element_by_css_selector('input[name="password"]'))
    password.send_keys(mypw)
except Exception as ex:
    print('비밀번호 입력 실패 >> ', ex)
    quit()

try :
    submit = WebDriverWait(driver, 10)\
        .until(lambda drv: drv.find_element_by_css_selector('button[type="submit"]'))
    submit.click()
except Exception as ex:
    print('로그인 버튼 클릭 실패 >> ', ex)
    #quit()

time.sleep(3)

driver.get('https://www.instagram.com/explore/tags/파이썬')
time.sleep(3)

img_list = []
for i in range(0, 5) :
    soup = bs(driver.page_source, 'html.parser')
    img = soup.select('img[srcset]')
    img_list += img
    
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
    time.sleep(3)

print(len(img_list))
driver.quit() 
    
src_list = []
for t in img_list :
    srcset = t.attrs['srcset']
    srcset_list = srcset.split(',')
    item = srcset_list[len(srcset_list) - 1]
    url = item[:item.find(" ")]
    src_list.append(url)
    
#print(src_list) 
    
datetime = dt.datetime.now().strftime('%y%m%d_%H%M')    
dirname = "insta_%s" %datetime

if not os.path.exists(dirname) :
    os.mkdir(dirname)
    
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

count = 0

for image_url in src_list:
    count += 1
    path = "%s/%04d.jpg" %(dirname, count)
    
    try :
        r = session.get(image_url, stream=True)
        if r.status_code != 200:
            raise Exception
            
        with open(path, 'wb') as f:
            f.write(r.raw.read())
            print(path, '---> 저장성공')
            
    except Exception as ex:
        print("######>> 저장실패", ex)
        continue
        
#print(path)  
    
    
    
    
    
    
    
    
    



