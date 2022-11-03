import sqlite3
conn = sqlite3.connect('sample.db')
cur = conn.cursor()

text = '''/help - помощь;\n/new_user - новый лог;\n/login - логгинг;'''

def helper():
    print(text)

class Shuffle:
    def __init__(self):
        self.alpha = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.itog = ''

    def cipher(self, to_sha, smeshenie):
        for i in to_sha:
            mesto = self.alpha.find(i)
            new_mesto = mesto + smeshenie
            if i in self.alpha:
                self.itog += self.alpha[new_mesto]
            else:
                self.itog += i
        return (self.itog)

    def decipher(self, to_sha, smeshenie):
        for i in to_sha:
            mesto = self.alpha.find(i)
            new_mesto = mesto - smeshenie
            if i in self.alpha:
                return(self.itog)
            return()

class NewUser:
    def __init__(self):
        self.login = input('Введите логин: ')
        self.pasw = input('Введите пароль: ')
        self.alternative = input('Введите ответ на альтернативный вопрос: ')

    def create(self, data = None):
        conn = sqlite3.connect(data)
        cur = conn.cursor()
        user = (self.login, self.pasw, self.alternative)
        cur.execute('''INSERT INTO users VALUES(?, ?, ?);''', user)
        conn.commit()

class Login:
    def __init__(self, db):
        self.database = db

    def insert_data(self):
        cur = conn.cursor()
        cur.execute('''SELECT login, pasw, alternative FROM users ''')

    def get_login(self, login_find):
        cur = sqlite3.connect(self.database).cursor()
        perpose = cur.execute(f'''SELECT login FROM users WHERE login LIKE "%{login_find}%"''').fetchone()
        if perpose == None:
            return

class Prof:
    def __init__(self, cursor, table):
        self.login = 'login'
        self.pasw = 'pasw'
        self.alternative = 'alternative'
        self.cur = cursor
        self.table = table

    def get_info_user(self):
        rows = self.cur.execute(f'SELECT {self.login}, {self.pasw}, {self.alternative} FROM {self.table}').fetchall()

        def log_in(rows):
            list_for_append = []
            for row in rows:
                list_for_append.append(row[0])
            print('Список логинов базы данных: '+ str(list_for_append))

        def pasw(rows):
            list_for_append = []
            for row in rows:
                list_for_append.append(row[1])
            print('Список паролей базы данных: '+ str(list_for_append))

        def alter(rows):
            list_for_append = []
            for row in rows:
                list_for_append.append(row[2])
            print('Список альтернативных ответов базы данных: '+ str(list_for_append))


        com_dict = {'/login': log_in,
                    '/pasw': pasw,
                    '/alter': alter}

        def income_function():
            com = input('/login, /pasw, /alter - ? \n')
            period = input('Следующий прогон будет? /next or /stop? ')
            if period == '/next':
                if com == '/login':
                    com_dict['/login'](rows)
                if com == '/pasw':
                    com_dict['/pasw'](rows)
                if com == '/alter':
                    com_dict['/alter'](rows)
                income_function()
            else:
                pass

        income_function()
