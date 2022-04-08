#!/usr/bin/python3
''' Script that takes an argument and display
 all values in the states '''

from sys import argv

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
