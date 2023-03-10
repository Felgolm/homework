# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number: int) -> str:
    num_to_word = {
        0: "Ноль", 1: "Один", 2: "Два", 3: "Три",
        4: "Четыре", 5: "Пять", 6: "Шесть",
        7: "Семь", 8: "Восемь", 9: "Девять"}

    try:
        return num_to_word[number]

    except Exception:
        return ("None")


# Проверка

for i in range(11):
    print(f'{i} - {switch_it_up(i)}')
