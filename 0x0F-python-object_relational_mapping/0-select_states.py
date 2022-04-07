#!/usr/bin/python3
''' Script that lists all states from database '''

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect("localhost", user, pswd, dbname)

    cursor = db.cursor()
    query = "SELECT * FROM states;"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
            print(item)
    except:
        print("Failed to fetch data")
    db.close()
