#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
    )
    cur = db.cursor()
    query = """SELECT cities.name
             FROM cities
             JOIN states ON states.id = cities.state_id
             WHERE states.name = %s
             ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))

    cur.close()
    db.close()
