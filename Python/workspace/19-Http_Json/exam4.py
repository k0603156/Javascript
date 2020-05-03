import requests
import json
from pandas import DataFrame

json_list_url = "http://192.168.0.96/students.json"

r = requests.get(json_list_url)

if r.status_code != 200 :
    print('[%dError] %s' %(r.status_code, r.reason))
    #quit()
    
result = json.loads(r.text)
print(result)
print('-' * 30)

df = DataFrame(result['students']['student'])
print(df)
print('-' * 30)
    


