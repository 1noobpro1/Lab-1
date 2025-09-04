str = input("Введите строку: ")
n = ' '

for char in str:
    if char.isdigit():
        n +=char
    else:
        if n!= ' ':
            print(n)
            n = ' '
if n !=' ':
    print(n)
