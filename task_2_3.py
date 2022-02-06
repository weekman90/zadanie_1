lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
lst2 = []
count = ''
lst3 = []

for i in lst:

    lst2.append([i[::]])                            # отделяю имена через реверс, каждой позиции
    count += i+' '
    name, *work = count[::-1].split()
    lst3.append(name[::-1])
    count = ''

lst2 = []

for i in lst3:

    count += i                                      #Привожу к 'Заглавным буквам'
    lst2.append(count.capitalize())
    count = ''

for name in lst2:
    print(f'Привет, {name}!')                       #вывод приветсвия