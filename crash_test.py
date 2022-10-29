def inside(cursor):
    rows = cursor.execute('SELECT login, pasw, alternative FROM users')
    for row in rows:
        print(row.fetcone())

def pr():
    lt = [1,2,3]
    a = 'Hey'
    print(str(lt) + a)


pr()