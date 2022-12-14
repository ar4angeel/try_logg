import sqlite3
from som_logg import (LoginCreate, Prof, helper)
conn = sqlite3.connect('sample.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users(login TEXT, pasw TEXT, alternative TEXT)''')

conn.commit()

cmd = input('Введите команду, которую хотите использовать: \n')

command_dict = {'/help': helper,
                '/new_user': LoginCreate,
                '/selector': Prof}

def income_func():
    if cmd == '/help':
        command_dict['/help']()
    if cmd == '/new_user':
        command_dict['/new_user']('sample.db').create_user()
    if cmd == '/selector':
        command_dict['/selector'](cur, 'users').get_info_user()

income_func()