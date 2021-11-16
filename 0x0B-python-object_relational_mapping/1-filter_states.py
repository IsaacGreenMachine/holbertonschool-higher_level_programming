#!/usr/bin/python3
"""list all states starting with N from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    userName = sys.argv[1]
    password = sys.argv[2]
    dataBaseName = sys.argv[3]
    db = MySQLdb.connect(db=dataBaseName, user=userName,
                         passwd=password, port=3306, host="localhost")
    dbcursor = db.cursor()
    dbcursor.execute("SELECT * FROM states "
                     "WHERE LEFT(states.name, 1) = 'N' "
                     "ORDER BY id ASC")
    result = dbcursor.fetchall()
    for i in result:
        print(i)
