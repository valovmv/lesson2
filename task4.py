my_str = input("Введите несколько слов: ")
word = []
num = 1
for b in range(my_str.count(' ') + 1):
    word = my_str.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [b]}")
        num += 1
    else:
        print(f" {num} {word [b] [0:10]}")
        num += 1