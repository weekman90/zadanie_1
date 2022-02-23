my_file=open(file='nginx_logs.txt', mode='r', encoding='utf-8')
content=my_file.readlines()
def gen_1 (content):
    rez=0                                       # не уверен, но вроде получилось)
    while rez<len(content):
        print((content[rez].split(' ')[0],content[rez].split('"')[1].split(' ')[0],content[rez].split('"')[1].split(' ')[1]))
        rez+=1

gen_1(content)
my_file.close()