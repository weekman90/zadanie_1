#number = int(input())
number = 1
sum_of_cube=0
while number <= 1000:
                                                         #хардкодим
    cube = number ** 3
    summary = ((cube // 1000000000) % 10
              + (cube // 100000000) % 10
              + (cube // 10000000) % 10
              + (cube // 1000000) % 10
              + (cube // 100000) % 10
              + (cube // 10000) % 10
              + (cube // 1000) % 10
              + (cube // 100) % 10
              + (cube // 10) % 10
              + cube % 10)

    if number % 2 > 0 and summary % 7 == 0:
        sum_of_cube +=number
        print(number, '^3: ', cube, 'sum: ', sum_of_cube, '[', summary, ']')
        number += 1

    else:
        number += 1
        pass