#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa by state"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    userName = sys.argv[1]
    password = sys.argv[2]
    dataBaseName = sys.argv[3]
    db = MySQLdb.connect(db=dataBaseName, user=userName,
                         passwd=password, port=3306, host="localhost")
    dbcursor = db.cursor()
    dbcursor.execute("SELECT cities.id, cities.name, states.name " +
                     "FROM cities RIGHT JOIN states " +
                     "ON cities.state_id = states.id " +
                     "ORDER BY id ASC")
    result = dbcursor.fetchall()
    for i in result:
        print(i)
    dbcursor.close()
    db.close()
