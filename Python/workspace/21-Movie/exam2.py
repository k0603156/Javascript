print(df)
print('-' * 30)

tmp_df = df.filter(['movieNm', 'audiCnt'])
print(tmp_df)
print('-' * 30)

daily_rank_df = tmp_df.rename(index=tmp_df['movieNm'],
                              columns={'audiCnt':'관람객'})
print(daily_rand_df)
print('-' * 30)

daily_rank_df.drop('movieNm', axis=1, inplace=True)
print(daily_rank_df)
print('-' * 30)

print(daily_rank_df['관람객'])
print('-' * 30)

daily_rank_df['관람객'] = daily_rank_df['관람객'].astype(int)
print(daily_rank_df['관람객'])
print('-' * 30)

daily_rank_df_sort = daily_rank_df.sort_values('관람객')
print(daily_rank_df_sort)
print('-' * 30)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 17
pyplot.rcParams['figure.figsize'] = (20, 12)

daily_rank_df_sort.plot.barh(rot=45)
pyplot.title('%s 박스오피스 순위' %yesterday_str)
pyplot.grid()
pyplot.savefig('박스오피스순위.png')
pyplot.show()








