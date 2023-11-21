import pandas as pd

df = pd.DataFrame({'team': ['A' ,'A' ,'B' ,'B' ,'C'], 'points': [25, 12, 15, 14, 19], 'assists': [5, 7, 7, 9, 12], 'rebounds': [11, 8, 10, 6, 6]})
#Условия
#df_stat = df[(df.points > 13) & (df.assists > 7)]
# df_stat = df[(df.team == 'A') & (df.points >= 15)]
# df_stat = df[(df.points > 13) | (df.assists > 7)]
# df_stat = df[(df.team == 'A') | (df.points >= 15)]
#filter_list =  [12, 14, 15]
#df_stat =  df[df.points.isin (filter_list)]
filter_list2 = ['A', 'C']
df_stat = df[ df.team.isin (filter_list2)]
print(df_stat)
