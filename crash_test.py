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
    print(type(privet[0]))

class Add:
    def __init__(self, a):
        self.sec = a

    def sum(self, b):
        self.b = b
        string = self.sec + self.b
        print(string)

pr()