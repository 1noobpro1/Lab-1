import datetime
import random
jewelry = {
    "кольцо": ["золото", 15000, 5],
    "серьги": ["серебро", 8000, 3],
    "подвеска": ["платина", 25000, 2],
    "браслет": ["золото", 20000, 4],
    "цепочка": ["серебро", 12000, 6]
}
cashier_name = "Лаптюхов К. А."
def print_receipt(cart):
    current_time = datetime.datetime.now()
    print("\n" + "=" * 40)
    print("ЮВЕЛИРНЫЙ МАГАЗИН 'БРИЛЛИАНТ'".center(40))
    print("=" * 40)
    print("Чек №: ",random.randint(1000, 9999))
    print("Дата: ", current_time.strftime('%d.%m.%Y %H:%M'))
    print("Кассир: ",cashier_name)
    print("-" * 40)

    total = 0
    for item in cart:
        name, qty, price = item
        cost = qty * price
        total += cost
        print(name, qty,"x", price, "=",cost)

    print("-" * 40)
    print("ИТОГО:", total)
    print("=" * 40)
    print("Спасибо за покупку!".center(40))
    print("=" * 40 + "\n")

cart = []

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Выход")
    choice = input("Выберите пункт меню: ")
    if choice == '1':
        print("Введите 0 для выхода в Меню")
        print("Список товаров:")
        for i, name in enumerate(jewelry, 1):
            print(i,".", name)
        name = input("Введите название изделия: ")
        if name in jewelry:
            print(name, "-", jewelry[name][0])
        elif name == "0":
            print("Выход в Меню...")
        else:
            print("Товар не найден!")

    elif choice == '2':
        print("Введите 0 для выхода в Меню")
        print("Список товаров:")
        for i, name in enumerate(jewelry, 1):
            print(i, ".", name)
        name = input("Введите название изделия: ")
        if name in jewelry:
            print(name, "-", jewelry[name][1], "руб.")
        else:
            print("Товар не найден!")

    elif choice == '3':
        print("Введите 0 для выхода в Меню")
        print("Список товаров:")
        for i, name in enumerate(jewelry, 1):
            print(i, ".", name)
        name = input("Введите название изделия: ")
        if name in jewelry:
            print(name, "-", jewelry[name][2]," шт.")
        else:
            print("Товар не найден!")

    elif choice == '4':
        print("Введите 0 для выхода в Меню")
        print("\nВся информация о товарах:")
        print("-" * 80)
        for name, info in jewelry.items():
            print(name, ": состав - ",info[0], ", цена - ",info[1], ", руб., количество -", info[2]," шт.")

    elif choice == '5':
        while True:
            print("Введите 0 для выхода в Меню")
            print("Список товаров, их состав, количество и цена:")
            for i, name in enumerate(jewelry, 1):
                print(i, ".", name)
            name = input("Введите название изделия: ")
            if name == "0":
                print("Выход в Меню...")
                break

            if name not in jewelry:
                print("Товар не найден!")
                continue

            try:
                qty = int(input("Введите количество: "))
            except ValueError:
                print("Ошибка ввода количества!")
                continue

            if qty <= 0:
                print("Количество должно быть положительным!")
                continue

            if qty > jewelry[name][2]:
                print("Недостаточно товара на складе!")
                continue

            jewelry[name][2] -= qty
            cart.append([name, qty, jewelry[name][1]])
            print("Товар добавлен в корзину!")

        if cart:
            print_receipt(cart)
            cart = []

    elif choice == '6':
        print("До свидания!")
        break

    else:
        print("Неверный пункт меню!")
