# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month: int) -> str:
    quarter_dict = {
        "Первый квартал": (1, 2, 3),
        "Второй квартал": (4, 5, 6),
        "Третий квартал": (7, 8, 9),
        "Четвертый квартал": (10, 11, 12)
    }

    months = {
        1: 'январь', 2: "февраль", 3: "март",
        4: "апрель", 5: "май", 6: "июнь",
        7: "июль", 8: "август", 9: "сентябрь",
        10: "октябрь", 11: "ноябрь", 12: "декабрь"}

    for quarter in quarter_dict.keys():
        if month in quarter_dict[quarter]:
            return f'{months[month].title()} - {quarter}' 
    
    return "Введены некорректные данные"
            

# Проверка:
monts_tuple = (x for x in range(0, 13))

for month in monts_tuple:
    print(f'{quarter_of(month)} \n')