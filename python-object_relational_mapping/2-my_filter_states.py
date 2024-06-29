#!/usr/bin/python3
"""
Sript that takes in an argument and displays all values in the state table
of hbtn_0e_0_usa where name matches the argument.
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
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY id ASC""".format(searched_state))
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
