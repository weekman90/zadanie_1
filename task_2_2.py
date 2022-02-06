lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
count = []
p = ''

edit_lst=[]                                             # не выполнил условия с отступами ковычек(
for i in lst:

    for j in i:

        for x in numbers:

            if j == x:

                count.append(j)

                if j == i[-1]:

                    for w in count:                     # пробегаемся по счётчику
                        for e in w:

                            p += e

                    if len(p)==1:

                        if i[0] == '-' or i[0] == '+':  # добавлям знак + или -
                            edit_lst.append('"')
                            edit_lst.append(i[0]+'0' + p)
                            edit_lst.append('"')
                            p = ''
                            count = []
                        else:
                            edit_lst.append('"')
                            edit_lst.append('0' + p)           # добавляем цифры из счётчика к отредактированному списку
                            edit_lst.append('"')
                            p = ''
                            count = []

                    else:
                        if i[0] == '-' or i[0] == '+':  # добавлям знак + или -
                            edit_lst.append('"')
                            edit_lst.append(i[0] + p)
                            edit_lst.append('"')
                            p = ''
                            count = []
                        else:
                            edit_lst.append('"')
                            edit_lst.append(p)                 # добавляем цифры из счётчика к отредактированному списку
                            edit_lst.append('"')
                            p = ''
                            count = []

            elif j != x and i[0] != '+' and i[0] != '-' and i not in edit_lst and j not in numbers:
                edit_lst.append(i)

print(lst)
print()
print(edit_lst)
print()

for i in edit_lst:
    count = str
    count = ' '.join(edit_lst)                                  #форматируем в текст

print(count)







