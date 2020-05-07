import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as bs
import pandas as pd
from matplotlib import pyplot

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

driver.find_element_by_css_selector('.btn_global').click()
time.sleep(3)

driver.get('https://order.pay.naver.com/home')

try:
    WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector('#_listContentArea'))
except Exception as ex:
    print('NaverPay 페이지의 소스코드 구성이 변경되어 크롤링이 불가능합니다. >>', ex)
    quit()

count = 0

while True :
    try :
        more_button = WebDriverWait(driver, 3).until(lambda x: x.find_element_by_css_selector('#_moreButton'))
        
        attrs = {}
        for item in more_button.get_property('attributes') :
            attrs[item['name']] = item['value']
            
        if 'style' in attrs:   # style='display:none'
            break
        
        driver.find_element_by_css_selector('.button_viewmore').click()
        count += 1
        print('%d회  more 버튼이 클릭되었습니다.' %count)
    except Exception as ex :
        print('more 버튼을 찾을 수 없습니다. >> ', ex)
        break

soup = bs(driver.page_source, 'html.parser')

goods = soup.select('.goods_pay_item')

driver.quit()

if not goods :
    print('네이버 패이를 통한 구매 내역이 없습니다.')
    quit()
    
#print(goods)
    
pay_list = []

for g in goods :
    name = g.select('.name')[0].text.strip()
    name = name.replace('\n', ' ')
    name = name.replace('\t', '')
    name = name.strip()    
    #print(name)
    
    price = g.select('.info > li:nth-of-type(1)')[0].text.strip()
    price = price.replace('상품금액', '')
    price = price.replace(',', '')
    price = price.replace('원', '')
    price = int(price)
    #print(price)
    
    date = g.select('.info > .date')[0].text.strip()
    date = date.replace('상품구매날짜', '')
    date = date.strip()
    
    seller = g.select('.seller')[0].text.strip()
    seller_tel = g.select('.tel')[0].text.strip()
    
    good_dict = {'구매날짜':date, '상품명':name, '금액':price,
                 '판매처':seller, '연락처':seller_tel}
    
    pay_list.append(good_dict)
    
#print(pay_list)

df = pd.DataFrame(pay_list)

#print(df['구매날짜'])
df['구매날짜'] = pd.to_datetime(df['구매날짜'], format=('%Y.%m.%d'))
#print(df['구매날짜'])

df.sort_values('구매날짜', inplace=True)

df['년/월'] = df['구매날짜'].dt.strftime('%Y/%m')

result_df = df.filter(['년/월', '금액'])
result_df = df.groupby('년/월').sum()

#print(result_df)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 16
pyplot.rcParams['figure.figsize'] = (12, 6)

result_df.plot(rot=30, marker='o')
pyplot.grid()
pyplot.title('네이버패이를 통한 지출현황')
pyplot.ylabel('가격')
pyplot.xlabel('년/월')

xpos = list(range(0, len(result_df.index)))
xvars = list(result_df.index)
pyplot.xticks(xpos, xvars)

for i, v in enumerate(list(result_df['금액'])) :
    txt = '%d원' %v
    pyplot.text(i, v, txt, fontsize=14, color='#ff0000',
                horizontalalignment='center',
                verticalalignment='bottom')

pyplot.show()















