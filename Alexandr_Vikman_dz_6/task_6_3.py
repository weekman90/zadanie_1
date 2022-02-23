users= open(file='task_3_users.csv', mode='r', encoding='utf-8')
hobby= open(file='task_3_hobby.csv', mode='r', encoding='utf-8')
result= open(file='task_3_rezult.txt', mode='at', encoding='utf-8')
list_users=users.readlines()
list_hobby=hobby.readlines()
result_dict={}

def list_gen (list_users, list_hobby):
    rez=0
    fio=''
    full_fio=[]

    while rez<len(list_users):

        for i in list_users[rez].split(','):
            fio+= (i[0])

            if len(fio)== 3:
                full_fio.append(fio)
                fio= ''
        result_dict.update({str(full_fio[rez].split(',')[0].strip()): list_hobby[rez].strip()})
        rez+= 1

    print(result_dict)
    result.write(str(result_dict))                      #запись в txt файл путём прибавления.

list_gen(list_users, list_hobby)
