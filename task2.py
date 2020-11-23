my_list = ['23', '12', '17', '8', '5', '1']
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        b = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = b
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        b = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = b
        i += 2
print(my_list)
