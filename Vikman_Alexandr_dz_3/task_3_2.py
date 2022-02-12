def num_translate_adv (eng_number):



    numbers = {'ноль': 'zero', 'один': 'one', 'два': 'two',     #словарь с числами
               'три': 'three', 'четыре': 'four',
               'пять': 'five', 'шесть': 'six', 'семь': 'seven',
               'восемь': 'eight', 'девять': 'nine'}

    if eng_number==eng_number.capitalize():                  #позже придумал дополнить словарь, но решаю через If else


        eng_number = eng_number.lower()                       #перевожу 'входные' в нижний регистр

        if eng_number in numbers.values():                    #поиск входного параметра в словаре
            for key, item in numbers.items():
                if eng_number == item:
                    return key.capitalize()

    else:

        eng_number = eng_number.lower()                       # перевожу 'входные' в нижний регистр

        if eng_number in numbers.values():                    # поиск входного параметра в словаре
            for key, item in numbers.items():
                if eng_number == item:
                    return key

a = num_translate_adv('One')                                                  #присвоение функции переменной
                                                                             #т.к. не знаю как ещё вывести 'none'
print(a)