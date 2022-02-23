from os.path import join
from sys import argv
total_list= open(file=join('.', 'bakery.csv'), mode='r', encoding='utf-8')
total_list.readline(0)
                                                    # 24.02.2022 0:05
def show(argv):                                 #Просидел пол дня, бесконечно извеняюсь
                                     #Не понял как реализовать диапозонный вывод через консоль
    for i in (total_list.readline().strip(',').split(',')):
        print(i)
    return 0

if __name__ == '__main__':
    import sys

    exit(show(sys.argv))