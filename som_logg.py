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
    def __init__(self):
        self.login_pass = False
        self.login_get = False
        self.pasw_get = False
        self.alternative_get = False
        self.userid_pass = False
        self.userid_get = False

    def insert_data(self, data, connection, cursor):
        conn = sqlite3.connect(data)
        cur = conn.cursor()
        cur.execute('''SELECT login, pasw, alternative FROM users''')

class Prof:
    def __init__(self, cursor, table):
        self.login = 'login'
        self.pasw = 'pasw'
        self.alternative = 'alternative'
        self.cur = cursor
        self.table = table

    def get_info_user(self):
        rows = self.cur.execute(f'SELECT {self.login}, {self.pasw}, {self.alternative} FROM {self.table}')
        for row in rows:
            print(row.fetchone())

