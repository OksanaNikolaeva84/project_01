# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

print("Пункт A.") 
sum_dlit = 0
sum_dlit += my_favorite_songs[0][1]
sum_dlit += my_favorite_songs[1][1]
sum_dlit += my_favorite_songs[2][1]

print(f'Три песни звучат {sum_dlit} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


print("Пункт B.")
sum_dlit = 0
sum_dlit += my_favorite_songs_dict['Waste a Moment']
sum_dlit += my_favorite_songs_dict['A Sorta Fairytale']
sum_dlit += my_favorite_songs_dict['In This World']

print(f'Три песни звучат {sum_dlit} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 





import datetime
import random


print("Пункт C и D для списка.")

sum_dlit_sec = datetime.timedelta()
random_songs = random.sample(my_favorite_songs,3)

for song in random_songs:
  time_is_sec = str(song[1])
  time_minutes = time_is_sec.split('.')[0]
  time_seconds = time_is_sec.split('.')[1]
  if len(time_seconds) == 1:
    time_seconds = f'{time_seconds}0'
  td = datetime.timedelta(minutes=int(time_minutes), seconds=int(time_seconds))
  sum_dlit_sec += td
  #time_lst = str(song[1]).split('.')
  #print(int(time_lst[0])*60 + int( int(time_lst[1])*10 if len(time_lst[1])<2 else time_lst[1]))
  #sum_dlit_sec += int(time_lst[0])*60 + int( int(time_lst[1])*10 if len(time_lst[1])<2 else time_lst[1])


print(f'Три песни звучат {sum_dlit_sec} минут')


print("Пункт C и D для словаря.")
sum_dlit_sec_dict = datetime.timedelta()
random_songs_dict = random.sample(list(my_favorite_songs_dict),3)
#print(random_songs_dict)
for song in random_songs_dict:
  time_is_sec = str(my_favorite_songs_dict[song])
  time_minutes = time_is_sec.split('.')[0]
  time_seconds = time_is_sec.split('.')[1]
  if len(time_seconds) == 1:
    time_seconds = f'{time_seconds}0'
  td = datetime.timedelta(minutes=int(time_minutes), seconds=int(time_seconds))
  sum_dlit_sec_dict += td
  
print(f'Три песни звучат {sum_dlit_sec_dict} минут')



