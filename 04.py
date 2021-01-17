my_list = [1, 4, 5, 12, 1, 12, 7, 38, 9, 5]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print (my_new_list)