#!/usr/bin/python3
"""displays values in states where name matches argument (no injections)"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    userName = sys.argv[1]
    password = sys.argv[2]
    dataBaseName = sys.argv[3]
    checkWord = sys.argv[4]
    db = MySQLdb.connect(db=dataBaseName, user=userName,
                         passwd=password, port=3306, host="localhost")
    dbcursor = db.cursor()
    dbcursor.execute("SELECT * FROM states "
                     "WHERE states.name = %s "
                     "ORDER BY id ASC", (checkWord,))
    result = dbcursor.fetchall()
    for i in result:
        print(i)
    dbcursor.close()
    db.close()
