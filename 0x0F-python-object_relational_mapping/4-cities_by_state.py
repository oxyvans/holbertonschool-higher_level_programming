#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]

try:
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cur = db.cursor()
    cur.execute("SELECT city.id, city.name, state.name FROM cities city, states state WHERE state.id = city.state_id ORDER BY city.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
    
except Exception:
    print("Error")