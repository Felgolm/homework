from random import choice
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
    three_random_songs = {}
    name = ''
    _time = 0.0
    while len(three_random_songs) != 3:
        match input_list:
            case list():
                name, _time = choice(input_list)

            case dict():
                name, _time = choice(list(input_list.items()))

        if name not in three_random_songs:
            three_random_songs[name] = _time
    return three_random_songs


def time_counter(song_list: dict) -> float:
    return sum(song_list.values())


def float_to_time(time_in_float: float) -> time:
    round_time = Decimal(time_in_float).quantize(Decimal("1.00"), ROUND_HALF_DOWN)

    _min, _sec = str(round_time).split(".")
    minutes = int(_min) + int(_sec) // 60
    seconds = int(_sec) % 60

    return time(minute=minutes, second=seconds)


def main(song_list: list | dict) -> None:
    choisen_songs = choice_songs(song_list)
    songs = choisen_songs

    time_in_float = time_counter(choisen_songs)
    _time = float_to_time(time_in_float)

    print("=" * 50)
    print(f'Бережно отобранные песни: {songs}\n'
          f"Общее время песен: {_time} минут")

    print("=" * 50 + "\n")


if __name__ == "__main__":
    print('From list:')
    main(my_favorite_songs)
    print('From dict:')
    main(my_favorite_songs_dict)
