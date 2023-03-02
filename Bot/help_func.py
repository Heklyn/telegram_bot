import numpy as np
import random


def vector(matrix, size):
    v = np.linalg.eig(np.asarray(list(map(int, matrix.split()))).reshape(-1, size))[1]
    ans = ""
    for i in range(len(v)):
        ans += f"Вектор {i + 1}:\n"
        for j in range(size):
            ans += f"{v[i][j]:.4}\n"
        ans += '\n'
    ans = ans[:-1]
    return ans


def determinant(matrix, size):
    return str(int(np.linalg.det(np.asarray(list(map(int, matrix.split()))).reshape(-1, size))))


def from_str_to_list_of_str(matrix, size):
    return np.asarray(matrix.split()).reshape(-1, size).tolist()


def from_str_to_list(matrix, size):
    return np.asarray(list(map(int, matrix.split()))).reshape(-1, size)


def random_nums(size):
    matrix = ' '.join([str(random.randrange(-100, 100)) for i in range(size * size)])
    return matrix


def random_matrix():
    size = random.randrange(3, 7)
    return random_nums(size), size


def change_n_row(matrix, size, nums, n):
    matrix_new = from_str_to_list_of_str(matrix, size)
    for i in range(size):
        matrix_new[n - 1][i] = str(nums[i])
    matrix_new = np.array(matrix_new).reshape(1, -1).tolist()
    text = ' '.join(matrix_new[0])
    return text


def change_n_column(matrix, size, nums, n):
    matrix_new = from_str_to_list_of_str(matrix, size)
    for i in range(size):
        matrix_new[i][n - 1] = str(nums[i])
    matrix_new = np.array(matrix_new).reshape(1, -1).tolist()
    text = ' '.join(matrix_new[0])
    return text


def rjust_space_custom(stroka, num):
    count = num - len(stroka)
    return '  ' * count + stroka
