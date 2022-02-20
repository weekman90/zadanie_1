# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
#
# groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
#
#
# def class_group_range(tutors, groups):
#     rez = 0
#     while rez < len(tutors):
#         yield tutors[rez], groups[rez]
#         rez += 1
#
#
# gen1 = class_group_range(tutors, groups)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']

groups = ['9А', '7В', '9Б', '9В']

def class_group_range(tutors, groups):
    rez = 0
    while rez < len(tutors):
        if rez<len(groups):

            yield tutors[rez], groups[rez]
            rez += 1

        else:

            yield tutors[rez], None
            rez += 1

gen1 = class_group_range(tutors, groups)


