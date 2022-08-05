#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]
    STATE = str(argv[4])

try:
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name=%s ORDER BY id ASC", (STATE,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
    
except Exception:
    print("Error")
