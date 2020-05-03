import numpy
from pandas import DataFrame
from matplotlib import pyplot
from pandas import read_excel

df = read_excel('data/시도별_월별_교통사고_20200327151519.xlsx')

col_list = list(df.columns)

df_traffic = df.filter(['시도별(1)','2017. 01', '2017. 02', '2017. 03', '2017. 04',
                        '2017. 05', '2017. 06', '2017. 07', '2017. 08',
                        '2017. 09', '2017. 10', '2017. 11', '2017. 12'])

col_list = list(df_traffic.columns)

df_traffic.drop(0, inplace=True)

df_traffic = df_traffic.rename(index=df_traffic['시도별(1)'])\
            .drop('시도별(1)', axis=1)

dic_month = {'2017. 01':'1월', '2017. 02':'2월', '2017. 03':'3월', 
             '2017. 04':'4월', '2017. 05':'5월', '2017. 06':'6월', 
             '2017. 07':'7월', '2017. 08':'8월', '2017. 09':'9월',
             '2017. 10':'10월', '2017. 11':'11월', '2017. 12':'12월'}

df_traffic.rename(columns=dic_month, inplace=True)

df_traffic = df_traffic.T

col_list = list(df_traffic.columns)

df_traffic.drop(['경기', '강원', '충북', '충남',
                 '전북', '전남', '경북', '경남', '제주', 
                 '광주', '대전', '울산', '세종'], axis=1, inplace=True)
print(df_traffic)
print('-' * 30)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 16
pyplot.rcParams['figure.figsize'] = (10, 6)

df_traffic['서울'].plot.barh(color='#0846EB', rot=0, width=0.7)
pyplot.grid()
pyplot.legend()
pyplot.title('2017년 서울의 월별 교통사고')
pyplot.ylabel('월')
pyplot.xlabel('교통사고 수')
pyplot.xlim(2500, 3700)

for i, v in enumerate(list(df_traffic['서울'])) :
    txt = '%d건' %v
    pyplot.text(v, i, txt, fontsize=14, color='#ff0000',
                horizontalalignment='left', 
                verticalalignment='center')
pyplot.show()

df_traffic.plot.barh(rot=0, width=0.7)
pyplot.grid()
pyplot.legend(bbox_to_anchor=(1, 0.65))
pyplot.title('2017년 월별 교통사고')
pyplot.ylabel('월')
pyplot.xlabel('교통사고 수')
pyplot.show()











