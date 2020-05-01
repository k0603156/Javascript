import requests

url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

r = session.get(url)
if r.status_code != 200 :
    print('[Error]')
    quit()
    
print(r.text)
print('-' * 30)

with open('naver급상승 검색어.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)


