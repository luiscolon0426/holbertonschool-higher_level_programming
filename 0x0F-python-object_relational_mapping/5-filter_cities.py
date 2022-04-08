#!/usr/bin/python3
''' Script that list all cities from that state as args '''

import MySQLdb
from sys import argv

if __name__ == "__main__":
        db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                            db=argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT cities.name "
                   "FROM cities "
                   "JOIN states "
                   "ON cities.state_id=states.id AND states.name=%s "
                   "ORDER BY cities.id ASC ", (argv[4],))
        rows = cursor.fetchall()
        print(", ".join(row[0] for row in rows))
        cursor.close()
        db.close()