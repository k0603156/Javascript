import requests
import json
from pandas import DataFrame
from matplotlib import pyplot

json_list_url = "http://192.168.0.96/student.json"

r = requests.get(json_list_url)

if r.status_code != 200 :
    print('[%d Error] %s' %(r.status_code, r.reason))
    quit()
    
result = json.loads(r.text)
print(result)
print(type(result))
print('-' * 30)

df = DataFrame(result['student'])
print(df)
print('-' * 30)

score_df = df.rename(index=df['name'],
                     columns={'eng':'영어','kor':'국어','math':'수학'})
print(score_df)
print('-' * 30)

score_df.drop('name', axis=1, inplace=True)
print(score_df)
print('-' * 30)

score_df = score_df.reindex(columns=['국어','영어','수학'])
print(score_df)
print('-' * 30)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 16
pyplot.rcParams['figure.figsize'] = (14, 8)

score_df.plot.bar(rot=0)
pyplot.grid()
pyplot.title('학생별 시험 점수')
pyplot.xlabel('학생명')
pyplot.ylabel('점수')
pyplot.show()










