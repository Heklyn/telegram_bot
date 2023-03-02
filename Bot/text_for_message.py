from help_func import rjust_space_custom

error_text = """
---------------
Неправильный ввод
        """

def message_start():
    text = """
Добро пожаловать
в <b>Heklyn_bot</b>!!!
"""
    return text


def message_description():
    text = """
Бот может посчитать дискриминант и собственные вектора матрицы, введенной пользователем
Для корректного отображения не рекомендуем вводить большие числа
Бот не предназначен для групп
"""
    return text


def message_help():
    text = """
/start - запуск бота
/help - список команд бота
/description - описание бота
"""
    return text


def message_set_size(error=False):
    text = """
Матрица еще не создана
---------------
Задайте размер матрицы:
(целое число от 2 до 9 включительно) 
"""
    if error:
        text += error_text
    return text


def message_out_matrix(matrix):
    size = len(matrix[0])
    sizes_of_nums = [[len(matrix[i][j]) for i in range(size)] for j in range(size)]
    max_sizes = [max(i) for i in sizes_of_nums]
    matrix_text = ""
    for item in matrix:
        matrix_text += " "
        for i in range(size):
            matrix_text += rjust_space_custom(item[i], max_sizes[i]) + '  '

        matrix_text += "\n"
    return matrix_text[:-1]


def message_main(matrix):
    text = """
Матрица:
"""
    text += message_out_matrix(matrix)
    return text

def message_change_all(error=False):
    text = """
---------------
Введите матрицу:
(целые числа через пробел, каждая строка на новой строчке
максимальный размер числа: не больше 19 значащих цифр)
"""
    if error:
        text += error_text
    return text


def message_choose_n_row(error=False):
    text = """
---------------
Введите номер строки:
(целое число, нуммерация с 1)
"""
    if error:
        text += error_text
    return text


def message_choose_n_column(error=False):
    text = """
---------------
Введите номер столбца:
(целое число, нуммерация с 1)
"""
    if error:
        text += error_text
    return text


def message_change_size(error=False):
    text = """
---------------
Введите размер матрицы:
(целое число от 2 до 9 включительно)  
"""
    if error:
        text += error_text
    return text


def message_determinant(value):
    text = f"""
---------------
Детерминант: {value}
"""
    return text


def message_vectors(value):
    text = f"""
---------------
{value}
"""
    return text


def message_change_row(error=False):
    text = """
---------------
Введите строку:
(целые числа в одной строке через пробел
максимальный размер числа: не больше 19 значащих цифр)  
"""
    if error:
        text += error_text
    return text


def message_change_column(error=False):
    text = """
---------------
Введите столбец:
(целые числа в одной строке через пробел
максимальный размер числа: не больше 19 значащих цифр)  
"""
    if error:
        text += error_text
    return text