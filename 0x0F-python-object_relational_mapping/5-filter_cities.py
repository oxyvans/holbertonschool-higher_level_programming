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
    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=DB)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                    LEFT JOIN states\
                        ON cities.state_id = states.id\
                            WHERE states.name=%s\
                                ORDER BY cities.id ASC", (STATE,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    
except Exception:
    print("Error")