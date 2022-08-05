#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    HOST = "localhost"
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]
    STATE = argv[4]


try:
    db = MySQL.connect(host=HOST, user=USER, passwd=PASS, db=DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".format(STATE))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    
except Exception:
    print("Error")