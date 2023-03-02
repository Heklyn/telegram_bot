from text_for_message import *
from sqlite import *
from keyboards import *
from help_func import *


def callback_answer(callback):
    chat_id = callback.message.chat.id
    message_text = callback.message.text.split('---------------')[0]

    if callback.data == 'set_size':
        update_stage(chat_id, '0.1')
        return message_set_size(), ikb_return

    elif callback.data == 'return':
        stage = get_chat_stage(chat_id).split('.')[0]
        update_stage(chat_id, f"{stage}.0")
        if stage == '0':
            return message_start(), ikb_start
        else:
            matrix = get_matrix(chat_id)
            size = get_size(chat_id)
            return message_main(from_str_to_list_of_str(matrix, size)), ikb_main

    elif callback.data == 'generate_random_matrix':
        matrix, size = random_matrix()
        update_matrix_with_size(chat_id, matrix, size)
        text = message_main(from_str_to_list_of_str(matrix, size))
        return text, ikb_main

    elif callback.data == 'random_nums':
        size = get_size(chat_id)
        matrix = random_nums(size)
        update_matrix(chat_id, matrix)
        text = message_main(from_str_to_list_of_str(matrix, size))
        return text, ikb_main

    elif callback.data == 'change_all':
        text = message_text + message_change_all()
        update_stage(chat_id, '1.1')
        return text, ikb_return

    elif callback.data == 'change_n_row':
        text = message_text + message_choose_n_row()
        update_stage(chat_id, '1.2')
        return text, ikb_return

    elif callback.data == 'change_n_column':
        text = message_text + message_choose_n_column()
        update_stage(chat_id, '1.4')
        return text, ikb_return

    elif callback.data == 'change_size':
        update_stage(chat_id, '1.6')
        text = message_text + message_change_size()
        return text, ikb_return

    elif callback.data == 'determinant':
        matrix = get_matrix(chat_id)
        size = get_size(chat_id)
        value = determinant(matrix, size)
        text = message_main(from_str_to_list_of_str(matrix, size)) + message_determinant(value)
        return text, ikb_main

    elif callback.data == 'vectors':
        matrix = get_matrix(chat_id)
        size = get_size(chat_id)
        value = vector(matrix, size)
        text = message_main(from_str_to_list_of_str(matrix, size)) + message_vectors(value)
        return text, ikb_main


def create_some_text(chat_id):
    matrix = get_matrix(chat_id)
    size = get_size(chat_id)
    return message_main(from_str_to_list_of_str(matrix, size))


def message_answer(msg):
    chat_id = msg.chat.id
    stage = get_chat_stage(chat_id)
    if stage == "0.1":
        try:
            size = int(msg.text)
        except:
            return message_set_size(True), ikb_return

        if 2 <= size <= 9:
            null_matrix(chat_id, size)
            return create_some_text(chat_id), ikb_main
        else:
            return message_set_size(True), ikb_return

    elif stage == "1.6":
        try:
            size = int(msg.text)
        except:
            return create_some_text(chat_id) + message_change_size(True), ikb_return

        if 2 <= size <= 9:
            null_matrix(chat_id, size)
            return create_some_text(chat_id), ikb_main
        else:
            return create_some_text(chat_id) + message_change_size(True), ikb_return

    elif stage == '1.2':
        try:
            n = int(msg.text)
        except:
            return create_some_text(chat_id) + message_choose_n_row(True), ikb_return

        size = get_size(chat_id)
        if 1 <= n <= size:
            update_row(chat_id, n)
            return create_some_text(chat_id) + message_change_row(), ikb_return
        else:
            return create_some_text(chat_id) + message_choose_n_row(True), ikb_return


    elif stage == '1.4':
        try:
            n = int(msg.text)
        except:
            return create_some_text(chat_id) + message_choose_n_column(True), ikb_return

        size = get_size(chat_id)
        if 1 <= n <= size:
            update_column(chat_id, n)
            return create_some_text(chat_id) + message_change_column(), ikb_return
        else:
            return create_some_text(chat_id) + message_choose_n_column(True), ikb_return


    elif stage == '1.3':
        try:
            nums = list(map(int, msg.text.split()))
        except:
            return create_some_text(chat_id) + message_choose_n_row(True), ikb_return

        size = get_size(chat_id)
        if len(nums) == size:
            matrix = get_matrix(chat_id)
            row = get_row(chat_id)
            matrix = change_n_row(matrix, size, nums, row)
            update_matrix(chat_id, matrix)
            return create_some_text(chat_id), ikb_main
        else:
            return create_some_text(chat_id) + message_choose_n_row(True), ikb_return


    elif stage == '1.5':
        try:
            nums = list(map(int, msg.text.split()))
        except:
            return create_some_text(chat_id) + message_choose_n_column(True), ikb_return

        size = get_size(chat_id)
        if len(nums) == size:
            matrix = get_matrix(chat_id)
            column = get_column(chat_id)
            matrix = change_n_column(matrix, size, nums, column)
            update_matrix(chat_id, matrix)
            return create_some_text(chat_id), ikb_main
        else:
            return create_some_text(chat_id) + message_choose_n_column(True), ikb_return

    elif stage == '1.1':
        try:
            nums = msg.text.split('\n')
            arr = []
            for item in nums:
                arr.extend(list(map(int, item.split())))
        except:
            return create_some_text(chat_id) + message_change_all(True), ikb_return
        size = get_size(chat_id)
        if len(arr) == size * size:
            arr = [str(i) for i in arr]
            matrix = ' '.join(arr)
            update_matrix(chat_id, matrix)
            return create_some_text(chat_id), ikb_main
        else:
            return create_some_text(chat_id) + message_change_all(True), ikb_return

    else:
        return '-1', None