import sqlite3
conn = sqlite3.connect('sample.db')
cur = conn.cursor()

text = '''/help - помощь;\n/new_user - новый лог;\n/login - логгинг;'''
login_main = 'login'
alter_main = 'alternative'
pasw_main = 'pasw'

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

# class NewUser:
#     def __init__(self):
#         self.login = input('Введите логин: ')
#         self.pasw = input('Введите пароль: ')
#         self.alternative = input('Введите ответ на альтернативный вопрос: ')
#
#     def create(self, data = None):
#         conn = sqlite3.connect(data)
#         cur = conn.cursor()
#         user = (self.login, self.pasw, self.alternative)
#         cur.execute('''INSERT INTO users VALUES(?, ?, ?);''', user)
#         conn.commit()

class LoginCreate:
    def __init__(self, db):
        self.database = db

    def get_something(self, what_get, what_find):
        line_getter = {login_main: None,
                            pasw_main: None,
                            alter_main: None}
        cur = sqlite3.connect(self.database).cursor()
        purpose = cur.execute(f'''SELECT {what_get} FROM users WHERE {what_get} LIKE "%{what_find}%"''').fetchone()
        if purpose == None:
            line_getter[what_get] = True
            return line_getter[what_get]
        if purpose == str:
            line_getter[what_get] = False
            return line_getter[what_get]

    def create_user(self):
        sub_login = input('Введите логин: ')
        sub_pasw = input('Введите пароль: ')
        sub_alter = input('Введите ответ на альтернативный вопрос: ')

        def create_login():
            if self.get_something(login_main, sub_login) == True:
                self.login = sub_login
                return self.login
            else:
                print('Такой логин уже существует.')

        def create_pasw():
            self.pasw = sub_pasw
            return self.pasw

        def create_alter():
            if self.get_something(alter_main, sub_alter) == True:
                self.alter = sub_alter
                return self.alter



        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        user = (create_login(), create_pasw(), create_alter())
        cur.execute('''INSERT INTO users VALUES(?, ?, ?);''', user)
        conn.commit()
        self.__delattr__(self.login)  #ошибка Unresolved attribute reference 'login' for class 'LoginCreate'
        self.__delattr__(self.pasw)   #ошибка Unresolved attribute reference 'login' for class 'LoginCreate'
        self.__delattr__(self.alter)  #ошибка Unresolved attribute reference 'login' for class 'LoginCreate'


class Prof:
    def __init__(self, cursor, table):
        self.login = login_main
        self.pasw = pasw_main
        self.alternative = alter_main
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
