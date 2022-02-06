price_lst = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]
price_lst2 = []
price_lst3 = []
price_lst_reverse = price_lst3.sort(reverse=True)          #Прошу прощения с реверс не разобрался, время поджимало
count = ''                                                 #Так же много условий не выполнил, т.к дочитал о них слишком поздно
                                                        # всё делал по методичке, сам. Коряво, уверен можно значительно -
for i in price_lst:                                     # красивее, но я к этому только иду.
    price_lst2.append([i])
print(price_lst2)

for i in price_lst2:                                    #присвоение '00' и наименование валют
    for j in i:
        j=float(j)
        count += str(j)
        rub, kop = count.split('.')
        price_lst3.append(f'{rub.zfill(2)} рублей {kop.zfill(2)} копеек,')
        # print((f'{rub.zfill(2)} рублей {kop.zfill(2)} копеек'),)
        count = ''

print(price_lst3)
price_lst3.sort()    # сортитровка по возрастанию
print(price_lst3)
print(price_lst_reverse)

