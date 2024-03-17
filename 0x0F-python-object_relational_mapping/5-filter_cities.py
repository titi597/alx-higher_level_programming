#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    cities = cur.fetchall()
    tmp = list(city[0] for city in cities)
    print(*tmp, sep=", ")

    cur.close()
    db.close()
