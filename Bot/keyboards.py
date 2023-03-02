from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikbb_set_size = InlineKeyboardButton(text='Задать размер матрицы',
                                             callback_data='set_size')

ikbb_random_matrix = InlineKeyboardButton(text='Сгенерировать случайную матрицу',
                                             callback_data='generate_random_matrix')

ikbb_return = InlineKeyboardButton(text='Назад',
                                   callback_data='return')

ikbb_random_nums = InlineKeyboardButton(text='Заполнить случайно',
                                        callback_data='random_nums')

ikbb_change_all = InlineKeyboardButton(text='Заполнить сразу',
                                        callback_data='change_all')

ikbb_change_n_row = InlineKeyboardButton(text='Заполнить n-ю строку',
                                        callback_data='change_n_row')

ikbb_change_n_column = InlineKeyboardButton(text='Заполнить n-й столбец',
                                        callback_data='change_n_column')

ikbb_change_size = InlineKeyboardButton(text='Изменить размер',
                                        callback_data='change_size')

ikbb_determinant = InlineKeyboardButton(text='Посчитать детерминант',
                                        callback_data='determinant')

ikbb_vectors = InlineKeyboardButton(text='Посчитать собственные вектора',
                                        callback_data='vectors')


ikb_start = InlineKeyboardMarkup()
ikb_start.add(ikbb_set_size)
ikb_start.add(ikbb_random_matrix)

ikb_return = InlineKeyboardMarkup()
ikb_return.add(ikbb_return)

ikb_main = InlineKeyboardMarkup(row_width=1)
ikb_main.add(ikbb_random_nums, ikbb_change_all,
             ikbb_change_n_row, ikbb_change_n_column,
             ikbb_change_size, ikbb_determinant, ikbb_vectors)