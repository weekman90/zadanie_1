def thesaurus(*args):
    names = {}                                   #создаю словарь

    for name in args:                           #проверяю наличие ключа в словаре и создаю новые

         if name[0] not in names.keys():
            names.update({name[0]:[name]})

         else:                                   #добавляю в уже существующие

            names[name[0]].append(name)

    list_names=list(names.keys())               #создаю список из словаря, что бы отсортировать .sort
    list_names.sort()
    for i in list_names:
        print(i, ':', names[i])                 #вывод результативного словаря


thesaurus("Иван", "Мария", "Петр", "Илья")     #применение функции