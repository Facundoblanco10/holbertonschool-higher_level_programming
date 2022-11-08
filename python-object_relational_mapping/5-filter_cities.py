#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':

    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2],
                          db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name"
                " FROM states, cities"
                " WHERE states.id = cities.state_id"
                " AND BINARY states.name = '{}'"
                " ORDER BY cities.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for idx, row in enumerate(rows):
        if idx != 0:
            print(", ", end='')
        print(f"{row[1]}", end='')
    print()
    cur.close()
    con.close()
