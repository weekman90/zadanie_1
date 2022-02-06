N = int(input('введите кол-во процентов: '))
if (N % 10 == 2 or N % 10 == 3 or N % 10 == 4) and N % 100 != 12 and N % 100 != 13 and N % 100 != 14:
    print(N, 'процента')
elif N % 10 == 1 and N%100 != 11:
    print(N, 'процент')
else:
    print(N, 'процентов')