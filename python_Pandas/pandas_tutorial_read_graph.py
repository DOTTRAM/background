import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names=['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])
# df = data.groupby(['North Amierica', 'South America', 'Africa', 'Europe', 'Asia', 'Astralia']['topic'].count())
# print(data.head())
# print(data.groupby(['my_datetime', 'event'])['topic'].count())

dif = data['topic'].value_counts() 
print(dif)
plt.figure(figsize=(8,4))
dif.plot.bar(color='xkcd:light violet')
plt.xlabel('Страны', fontsize=30) #Подпись для оси х
plt.ylabel('Количество клиентов', fontsize=30) #Подпись для оси y
plt.title(' Общее количество клиентов по странам',fontsize=30) #Название
plt.subplots_adjust(bottom=0.250)
plt.show()

# x = data['topic']
# y = data.count('topic')
# plt.xlabel('Дата')
# plt.ylabel('Страны')
# plt.title('Анализ клиентов из  стран')
# plt.plot(x, y)
# plt.show()

e3
