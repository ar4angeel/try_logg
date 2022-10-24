import sqlite3
from som_logg import (NewUser, Prof, helper)
conn = sqlite3.connect('sample.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users(login TEXT, pasw TEXT, alternative TEXT)''')

conn.commit()

cmd = input('Введите команду, которую хотите использовать: \n')

command_dict = {'/help': helper(),
                '/new_user': NewUser().create(data = 'sample.db')}

def income_func():
    if cmd == '/help':
        command_dict['/help']
    elif cmd == '/new_user':
        command_dict['/new_user']

if __name__ == '__main__':
 income_func()
