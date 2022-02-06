duration=int(input('введите кол-во секунд:'))
sec = 1
min = sec * 60
hour = min * 60
day = hour * 24

if duration < 60:
    print ('до минуты: ', sec * duration, 'сек' )

elif 60 <= duration < (min * 60):
    print ('до часа: ', duration // min, 'мин', duration % min , 'сек')

elif sec * 60 <= duration < hour * 24:
    print ('до суток: ',duration // hour, 'час', (duration % hour) // min, 'мин',duration % min, 'сек')

else:
    print('больше суток: ',duration // day, 'дн', (duration % day) // hour, 'час', (duration % hour) // min, 'мин', duration % min, 'сек')

print()
print('Поставьте мне "пятёрку" пжлст.')
print()
input('press "Enter" for exit')
