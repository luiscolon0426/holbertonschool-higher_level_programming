#!/usr/bin/python3
''' Script that lists all cities from the database '''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset='utf8')
    cursor = db.cursor()
    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities,\
                 states WHERE states.id=state_id')
    table = cursor.fetchall()
    for row in table:
        print(row)
    cursor.close()
    db.close()
