#!/usr/bin/python3
"""
script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    cn = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = cn.cursor()
    cur.execute('SELECT * FROM states WHERE states.name'
                ' LIKE "[Nn]%" ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    cn.close()
