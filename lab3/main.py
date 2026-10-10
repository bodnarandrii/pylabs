def task_1():
    print("\n--- Завдання 1: Впорядкування рядків матриці за характеристиками ---")
    try:
        n = int(input("Введіть розмірність матриці n (n <= 15): "))
        if not (1 <= n <= 15):
            print("Помилка: n має бути в межах від 1 до 15.")
            return
    except ValueError:
        print("Некоректне значення.")
        return

    print(f"Введіть елементи матриці {n}x{n} (по {n} чисел у рядку через пробіл):")
    matrix = []
    for i in range(n):
        while True:
            row_input = input(f"Рядок {i + 1}: ").strip().split()
            if len(row_input) == n:
                try:
                    matrix.append([float(x) for x in row_input])
                    break
                except ValueError:
                    print(f"Помилка: введіть коректні дійсні або цілі числа.")
            else:
                print(f"Потрібно ввести рівно {n} чисел.")

    # Функція для обчислення суми модулів від'ємних елементів вектора
    def row_characteristic(row):
        return sum(abs(x) for x in row if x < 0)

    # Процедура перетворення матриці
    def sort_matrix_by_characteristics(mat):
        mat.sort(key=row_characteristic)

    sort_matrix_by_characteristics(matrix)

    print("\nПеретворена матриця (у порядку неспадання характеристик):")
    for row in matrix:
        char_val = row_characteristic(row)
        formatted_row = " ".join(f"{x:8.2f}" for x in row)
        print(f"{formatted_row}  | Характеристика: {char_val:.2f}")


def task_2():
    print("\n--- Завдання 2: Середня вартість журналів з тиражем < 10000 ---")
    n = 5
    prices_under_10k = []

    print(f"Введіть дані для {n} журналів:")
    for i in range(n):
        while True:
            try:
                line = input(f"Журнал {i + 1} (введіть ціну та тираж через пробіл): ").strip().split()
                if len(line) != 2:
                    print("Потрібно ввести два значення: ціну та тираж.")
                    continue
                price = float(line[0])
                circulation = int(line[1])
                if price < 0 or circulation < 0:
                    print("Ціна та тираж не можуть бути від'ємними.")
                    continue

                if circulation < 10000:
                    prices_under_10k.append(price)
                break
            except ValueError:
                print("Некоректний формат чисел. Спробуйте ще раз.")

    if prices_under_10k:
        avg_price = sum(prices_under_10k) / len(prices_under_10k)
        print(f"\nСередня вартість журналів з тиражем менше 10000 примірників: {avg_price:.2f}")
    else:
        print("\nЖурналів з тиражем менше 10000 примірників не знайдено.")


def task_3():
    print("\n--- Завдання 3: База даних продажів інтернет-магазину ---")
    print("Вводьте записи у форматі: <Покупець> <Товар> <Кількість>")
    print("Щоб завершити введення даних, введіть порожній рядок або 'END'.\n")

    database = {}

    while True:
        line = input().strip()
        if not line or line.upper() == "END":
            break

        parts = line.split()
        if len(parts) != 3:
            print("Некоректний формат рядка. Спробуйте ще раз (наприклад: Ivanov paper 10)")
            continue

        buyer, item, count_str = parts
        try:
            count = int(count_str)
        except ValueError:
            print("Кількість товару повинна бути цілим числом.")
            continue

        if buyer not in database:
            database[buyer] = {}

        database[buyer][item] = database[buyer].get(item, 0) + count

    print("\nРезультат:")
    for buyer in sorted(database.keys()):
        print(f"{buyer}:")
        items = database[buyer]
        for item in sorted(items.keys()):
            print(f"{item} {items[item]}")


def main():
    while True:
        print("\n" + "=" * 40)
        print("                 МЕНЮ                   ")
        print("=" * 40)
        print("1. Завдання 1 (Матриця та характеристики рядків)")
        print("2. Завдання 2 (Журнали та тираж)")
        print("3. Завдання 3 (Продажі інтернет-магазину)")
        print("0. Вихід")
        print("=" * 40)

        choice = input("Оберіть пункт меню (0-3): ").strip()

        if choice == "1":
            task_1()
        elif choice == "2":
            task_2()
        elif choice == "3":
            task_3()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір. Введіть цифру від 0 до 3.")


if __name__ == "__main__":
    main()