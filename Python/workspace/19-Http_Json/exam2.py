import requests
import json
from pandas import DataFrame

simple_json_url = "http://192.168.0.96/simple.json"

r = requests.get(simple_json_url)

if r.status_code != 200 :
    print('[%d Error] %s' %(r.status_code, r.reason))
    quit()
    
print(r.text)
print('-' * 30)

result = json.loads(r.text)
print(result)
print(type(result))
print('-' * 30)

df = DataFrame([result])
print(df)
print('-' * 30)

from matplotlib import pyplot
from matplotlib.image import imread

img = imread(df.loc[0, 'img'])
pyplot.imshow(img)
pyplot.axis('off')
pyplot.show()










