#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', username = sys.argv[1], password = sys.argv[2], database = sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
     for row in rows:
        print(row)
     c.close()
     db.close()


