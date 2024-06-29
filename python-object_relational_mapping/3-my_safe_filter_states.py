#!/usr/bin/python3
"""
Preventing SQL injection by Parametrized Queries
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    searched_state = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (searched_state,))
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
