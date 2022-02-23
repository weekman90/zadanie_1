from sys import argv
from os.path import join
total_list= open(file=join('.', 'bakery.csv'), mode='at', encoding='utf-8')
def add_sale(argv):
    program, *args = argv
    result = sum(map(int, args))
    total_list.write(str(result)+',')
    print(f'было добавленно: {result}')

    return 0

if __name__ == '__main__':
    import sys

    exit(add_sale(sys.argv))