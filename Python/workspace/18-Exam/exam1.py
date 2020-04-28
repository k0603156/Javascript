from pandas import DataFrame

hero_list = ['아이언맨','아이언맨','아이언맨','캡틴아메리카','캡틴아메리카',
             '캡틴아메리카','캡틴아메리카','블랙위도우','블랙위도우','토르',
             '헐크','헐크'];

df_hero = DataFrame(hero_list, columns=['이름'])
print(df_hero)
print('-' * 30)

count_str = df_hero['이름'].value_counts()
print(count_str)
print(type(count_str))
print('-' * 30)

df_count = DataFrame(count_str)
print(df_count)
print('-' * 30)

df_count.rename(columns={'이름':'득표수'}, inplace=True)
print(df_count)
print('-' * 30)

df_sort = df_count.sort_index()
print(df_sort)
print('-' * 30)

df_sort = df_count.sort_index(ascending=False)
print(df_sort)
print('-' * 30)

df_sort = df_count.sort_values('득표수')
print(df_sort)
print('-' * 30)




