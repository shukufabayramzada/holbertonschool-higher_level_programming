#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
    )
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
             FROM cities INNER JOIN states ON states.id = cities.state_id
             ORDER BY cities.id ASC"""
    cur.execute(query)
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
