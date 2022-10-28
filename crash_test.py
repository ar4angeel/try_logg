def inside(cursor):
    rows = cursor.execute('SELECT login, pasw, alternative FROM users')
    for row in rows:
        print(row.fetcone())