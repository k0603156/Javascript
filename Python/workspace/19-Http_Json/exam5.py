import requests
import json
from pandas import DataFrame
from matplotlib import pyplot

file_url = "http://192.168.0.96/grade.csv"

r = requests.get(file_url, stream=True)

if r.status_code != 200 :
    print('[Error]')
    quit()
    
data = r.raw.read()
print(data)
print('-' * 30)

with open('grade.csv', 'wb') as f:
    f.write(data)















