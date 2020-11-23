goods = int(input("Введите количество товаров: "))
n = 1
my_dict = []
my_list = []

while n <= goods:
    my_dict = dict({'Наименование': input("Введите наименование продукта: "), 'Цена': input("Введите цену: "),
                    'Количество': input('Введите количество продукта: '), 'eд': input("Введите единицу измерения: ")})
    my_list.append((n, my_dict))
    n += 1

print(my_list)
