#1. Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield, полностью истощить генератор.
# Формат вывода результата:
#
# Программа явно должна закончиться на StopIteration
# Техническое задание
#
# n - любое положительное число.
# Не путайте истощение итератора и печать его значений. Явно дойдите до StopIteration. Истощение генератора - любым удобным для вас способом. Например создаем генератор в программе, а истощаем руками в консоли или через цикл.
# Создание генератора сделайте внутри функции iterator_without_yield(n), примающей аргументом n любое положительное число и возвращающей генератор.


n=10
gen1=(i for i in range(n) if i%2==1)
for i in gen1:
    print (i)
print(next(gen1))

# n=10                                                      #проба через while
# gen1=(i for i in range(n) if i%2==1)
# while True:
#     next(gen1)
# print(next(gen1))



