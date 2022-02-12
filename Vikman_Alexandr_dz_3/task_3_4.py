def thesaurus_adv(*args):
    names_dict = {}                      #создаю словарь

    for i in args:                          #пробегаюсь по входным данным
        name, last_name = i.split(' ')          #делю на имя - фамилию
        l0=last_name[0]                     #первым буквам имени и фамилии присваиваю значения
        n0=name[0]                          #
        for y in args:
            if l0 not in names_dict:            # проверка на наличие Литерала фамилии
                names_dict.update({l0:{}})
            elif n0 not in names_dict[l0]:          #проверка на наличие Литерала имени
                names_dict[l0].update({n0:[]})
            elif n0 in names_dict[l0]:                  #проверка на наличие имени в списке
                if name not in names_dict[l0][n0]:
                    names_dict[l0][n0].append(name)
                else:
                    pass



    for i in names_dict.items():                            #вывожу по-строчно
        print(i,'\n')


thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
              "Петр Алексеев", "Илья Иванов", "Анна Савельева",
              "Василий Суриков")                                            # применение функции