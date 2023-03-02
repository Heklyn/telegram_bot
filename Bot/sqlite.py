import sqlite3 as sq


def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS matrices(chat_id TEXT PRIMARY KEY, matrix_size INTEGER, matrix_num TEXT, "
                "stage TEXT, message_id TEXT, row INTEGER, column INTEGER)")
    db.commit()


def is_chat_in_db(chat_id):
    chat = cur.execute(f"SELECT 1 FROM matrices WHERE chat_id == "
                       f"'{chat_id}'").fetchone()
    return True if chat else False


def create_matrix_for_new_chat(chat_id, msg_id):
    cur.execute("INSERT INTO matrices VALUES(?, ?, ?, ?, ?, ?, ?)",
                (chat_id, None, '', '0.0', msg_id, None, None))
    db.commit()


def null_user(chat_id, msg_id):
    update_matrix(chat_id, '')
    update_size(chat_id, None)
    update_msg(chat_id, msg_id)
    update_row(chat_id, None)
    update_column(chat_id, None)
    update_stage(chat_id, '0.0')


def null_matrix(chat_id, size):
    update_matrix_with_size(chat_id, ' '.join(['0'] * size * size), size)


def get(chat_id, column):
    value = cur.execute(f"SELECT {column} FROM matrices WHERE chat_id = '{chat_id}'").fetchone()
    return value


def get_chat_stage(chat_id):
    return get(chat_id, 'stage')[0]


def get_msg_id(chat_id):
    return int(get(chat_id, 'message_id')[0])


def get_row(chat_id):
    return int(get(chat_id, 'row')[0])


def get_column(chat_id):
    return int(get(chat_id, 'column')[0])


def get_matrix(chat_id):
    return get(chat_id, 'matrix_num')[0]


def get_size(chat_id):
    return int(get(chat_id, 'matrix_size')[0])


def update(chat_id, column, value):

    if value:
        #
        cur.execute(f"UPDATE matrices SET {column} = {value} WHERE chat_id == '{chat_id}'")
        db.commit()
    else:
        #
        cur.execute(f"UPDATE matrices SET {column} = null WHERE chat_id == '{chat_id}'")
        db.commit()


def update_str(chat_id, column, value):
    cur.execute(f"UPDATE matrices SET {column} = '{value}' WHERE chat_id == '{chat_id}'")
    db.commit()


def update_stage(chat_id, stage):
    update_str(chat_id, 'stage', stage)


def update_row(chat_id, row):
    update(chat_id, 'row', row)
    update_stage(chat_id, '1.3')


def update_column(chat_id, column):
    update(chat_id, 'column', column)
    update_stage(chat_id, '1.5')


def update_matrix(chat_id, matrix):
    update_str(chat_id, 'matrix_num', matrix)
    update_stage(chat_id, '1.0')


def update_size(chat_id, size):
    update(chat_id, 'matrix_size', size)


def update_msg(chat_id, msg):
    update_str(chat_id, 'message_id', msg)


def update_matrix_with_size(chat_id, matrix, size):
    update_size(chat_id, size)
    update_matrix(chat_id, matrix)
