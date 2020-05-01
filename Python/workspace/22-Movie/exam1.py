import requests
import json
import datetime as dt
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot

api_key = 'ba4'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt={date}'

df = DataFrame()

for i in range(-7, 0) :
    today = dt.datetime.now()
    delta = dt.timedelta(days=i)
    yesterday = today + delta
    yesterday_str = yesterday.strftime('%Y%m%d')
    #print(yesterday_str)
    
    api_uri = url.format(key=api_key, date=yesterday_str)
    #print(api_uri)
    
    r = session.get(api_uri)
    
    if r.status_code != 200 :
        print('[ERROR]')
        continue

    #print(r.text)
        
    daily_boxoffice_dict = json.loads(r.text)
    daily_df = DataFrame(daily_boxoffice_dict['boxOfficeResult']['dailyBoxOfficeList'])
    tmp_df = daily_df.filter(['movieNm','audiCnt'])
    #print(tmp_df)

    daily_rank_df = tmp_df.rename(index=tmp_df['movieNm'],
                                  columns={'audiCnt':yesterday_str})
    daily_rank_df.drop('movieNm', axis=1, inplace=True)
    #print(daily_rank_df)

    daily_rank_df[yesterday_str] = daily_rank_df[yesterday_str].astype(int)
    #print(daily_rank_df[yesterday_str])

    df = pd.merge(df, daily_rank_df, left_index=True, right_index=True, how="outer")

#print(df)
final_df = df.fillna(0)

yesterday = dt.datetime.now() + dt.timedelta(days = -1)
yesterday_str = yesterday.strftime('%Y%m%d')

final_df = final_df.sort_values(yesterday_str, ascending=False).head(5)
#print(final_df)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 17
pyplot.rcParams['figure.figsize'] = (20, 10)

final_df.plot.bar(rot=45)
pyplot.title('날짜별 관람객 빈도')
pyplot.show()

final_df.T.plot(rot=45)
pyplot.title('일주일간의 영화별 관람객 수 변화')
pyplot.show()








