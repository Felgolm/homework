# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

def day_in_month(day: int) -> str:
    months = {
        1: "31 день",    # январь
        2: "28 дней",    # февраль 
        3: "31 день",    # март
        4: "30 дней",    # апрель 
        5: "31 день",    # май 
        6: "30 дней",    # июнь
        7: "31 день",    # июль
        8: "31 день",    # август 
        9: "30 дней",    # сентябрь
        10: "31 день",   # октябрь
        11: "30 дней",   # ноябрь
        12: "31 день"    # декабрь
        }

    return months.get(day, "Такого месяца нет!")
# Проверка:

count = 0
while count != 13:
    count += 1
    print(f'Inpit: {count}, Output: {day_in_month(count)}')