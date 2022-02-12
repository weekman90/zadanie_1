def num_translate (eng_number):

    eng_number = eng_number.lower()                                      #перевожу 'входные' в нижний регистр

    numbers = {'ноль': 'zero', 'один': 'one', 'два': 'two',              #словарь с числами
               'три': 'three', 'четыре': 'four',
               'пять': 'five', 'шесть': 'six', 'семь': 'seven',
               'восемь': 'eight', 'девять': 'nine'}

    if eng_number in numbers.values():                                  #поиск входного параметра в словаре
        for key, item in numbers.items():
            if eng_number == item:
                return key

a = num_translate('nine')                                                  #присвоение функции переменной
                                                                        #т.к. не знаю как ещё вывести 'none'
print(a)