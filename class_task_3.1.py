# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)



from typing import List, Optional


class Matrix:
    def __init__(self, column: int, line: int):
        self.column = column
        self.line = line
        self.struct = self.create_matrix(self.column, self.line)

    def create_matrix(self, column: int, line: int) -> List[List[int]]:
        """ Генерирует матрицу по заданным параметрам """
        
        mcolumn = list(range(1, column + 1))
        return [mcolumn.copy() for _ in range(1, line + 1)]

    @property
    def show_structure(self):
        """ Возвращает число столбцов, строк матрицы. Выводит её структуру """
        
        print(f"column: {self.column} \nline: {self.line} \n")
        for i in self.struct:
            print(i)

    def set_digit(self, column: int, line: int, digit: Optional[int]):
        """ Изменяет число в заданной позийии """    
        
        if type(digit) == int or digit is None:
            self.struct[line-1][column-1] = digit
        else:
            print("Могут быть внесены данные типа int или None") #   raise ValueError("Могут быть внесены данные только типа int или None.")

    def __repr__(self) -> str:
        return f'{self.struct}'


class Table:
    def __init__(self, colnames: list):
        self.colnames = colnames
        self.rows = []

    def add_row(self, row: dict):
        if any(colname not in tuple(row) for colname in self.colnames):  # хотя бы один элемент не соответствует
            print('Такой колонки нет')
        else:
            self.rows.append(row)

    def get_column(self, colname):
        if (colname not in self.colnames):
            print('Такой колонки нет')
        return [r[colname] for r in self.rows]


    def sum(self, colname: str):
        if colname not in self.colnames:
          print('Неправильный формат')
        return sum([r[colname] for r in self.rows])
    
    # Рецепт велоспеда:
    # Принять число колон и строк. Создать таблицу, где число колонок и строк равна заданным значениям
    # Верхний ряд является справочным и отражает букву. Если количества букв не хватает для отображения количества столбцов, буквы будут составляться в пары (A, AA, AB, ABC)
    # Первая ячейки в строке является справочной и отражает цифру.
    # Чтобы выбрать ячейку, нужно задать букву и цифру


if __name__ == "__main__":
    
# Проверка матрицы:
    print('Создаём матрицу 5 х 5')
    matrix = Matrix(column=5, line=5)
   
    print('Cмотрим на полученную матрицу:')
    matrix.show_structure  # показывает число колонок, строк и структуру матрицы
    
    print('\nЗадаём значение "None" в позицию 3:3 ->')
    matrix.set_digit(column=3, line=3, digit=None)  # Задаём новое число
    matrix.show_structure  # Проверяем
    
    print('\nЗадаём значение "10" в позицию 5:2 ->')
    matrix.set_digit(column=5, line=2, digit=10)  # Задаём еще одно число
    matrix.show_structure  # Проверяем

    print('\nПробуем задать строковое значение в позицию 5:5 ->')
    matrix.set_digit(column=5, line=5, digit="None")  # вызываем ошибку. Для демонстрации заменено принтом

# Проверка Таблицы:
    # TODO - сделать класс таблицы
table1 = Table(['a', 'b'])
table1.add_row({'a': 1, 'b': 2})
table1.add_row({'a': 2, 'b': 4})
table1.add_row({'a': 3, 'b': 8})
table1.add_row({'a': 4, 'b': 16})
print(table1.get_column('a'))
print(table1.get_column('b'))
print(table1.rows)

# Хотели сделать таблицу.
# вариант с созданием таблицы можно реализовать, например через словари. Они будут в качестве строк.
# Можно попробовать сделать ключ в качестве имени колонки, значение в качестве всей колонки





