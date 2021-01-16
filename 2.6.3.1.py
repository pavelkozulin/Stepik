text = input()
value = input()
my_list = [x for x in text.split(' ')]
#print(my_list)
for i in range(len(my_list)):
    if my_list[i] == value:
        print(i, end = ' ')
if value not in my_list:
    print('Отсутствует')