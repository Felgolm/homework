# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace("!", "")


# Проверка
print("Задание A:")
strins = ("Hi! Hello!", "", "Oh, no!!!")
for i in strins:
    print(f'{i} -> {remove_exclamation_marks(i)}')


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s: str) -> str:
    if s[-1] == '!':
        return s[0:-1]
    return s


# Проверка
print("\n" + "Задание B:")
strings = ("Hi!", "Hi!!!", "!Hi")
for i in strings:
    print(f'{i} -> {remove_last_em(i)}')


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


def remove_word_with_one_em(received_string: str):
    received_string = received_string.split(" ")
    new_string = ''
    for ch in received_string:
        if ch.count('!') != 1:
            new_string += ch
    return new_string


# # Проверка:
string_list = ("Hi!", "Hi! Hi!", "Hi! Hi! Hi!",
               "Hi Hi! Hi!", "Hi! !Hi Hi!", "Hi! Hi!! Hi!", "Hi! !Hi! Hi!")

solutions = ('""', '""', '""', '"Hi"', '""', '"Hi!!"', '"!Hi!"')
print("\n" + "Задание C:")

for i in range(len(string_list)):
    print(f'{string_list[i]} -> {remove_word_with_one_em(string_list[i])}', end=' || ')
    print(f"Должно быть: {solutions[i]}")
