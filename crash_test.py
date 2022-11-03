import sqlite3

def inside(cursor):
    rows = cursor.execute('SELECT login, pasw, alternative FROM users')
    for row in rows:
        print(row.fetcone())

def pr():
    opt = input()
    cur = sqlite3.connect('sample.db').cursor()
    priv = cur.execute(f'''SELECT login FROM users WHERE login LIKE "%{opt}%"''')
    print(priv)
    privet = priv.fetchone()
    print(privet[0])

class Add:
    def __init__(self, a):
        self.sec = a

    def sum(self, b):
        self.__setattr__(Add,sec,b)
        string = self.a + self.b
        print(string)