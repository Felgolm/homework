from random import sample
from datetime import time
from decimal import Decimal, ROUND_HALF_DOWN

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 


def choice_songs(input_list: list | dict) -> dict:
    """ Принимает list или dict. Возвращает dict с тремя песнями """
    three_random_songs = {}
    
    match input_list:
        case list():
            items = sample(input_list, 3)
            for i in items:
                three_random_songs[i[0]] = i[1]

        case dict():
            # binary repitor: a = {'a': 1}
            #                 a |= {'b' : 2} => {'a': 1, 'b': 2}
            three_random_songs |= sample(sorted(input_list.items()), 3)
            # three_random_songs.update(sample(sorted(input_list.items()), 3))

    return three_random_songs


def time_counter(song_list: dict) -> float:
    """ Суммирует общее время песен """
    return sum(song_list.values())


def float_to_time(float_time: float) -> time:
    """ Конвертирует значение float в time """

    round_time = Decimal(float_time).quantize(Decimal("1.00"), ROUND_HALF_DOWN)

    _min, _sec = str(round_time).split(".")
    minutes = int(_min) + int(_sec) // 60
    seconds = int(_sec) % 60
    return time(minute=minutes, second=seconds)


def main(song_list: list | dict) -> None:
    # 1. Бережно отбираем песни
    random_songs = choice_songs(song_list)
    
    # 2. Сохраняем наименования для вывода
    song_names = ', '.join(random_songs)
    
    # 3. Подсчитываем общее время
    float_time = time_counter(random_songs)
    
    # 4. Переводим время в формат 'time'
    _time = float_to_time(float_time)

    print("=" * 80 + 
          f'\nБережно отобранные песни: {song_names}\nОбщее время песен: {_time} минут\n' +
          "=" * 80 + "\n")


if __name__ == "__main__":
    print('From list:')
    main(my_favorite_songs)

    print('From dict:')
    main(my_favorite_songs_dict)
