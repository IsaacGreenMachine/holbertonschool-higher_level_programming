#!/usr/bin/python3
"""lists all cities of argument's state using hbtn_0e_4_usa"""
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
    dbcursor.execute("SELECT cities.name " +
                     "FROM cities RIGHT JOIN states " +
                     "ON cities.state_id = states.id " +
                     "WHERE states.name = %s", (checkWord,))
    result = dbcursor.fetchall()
    for i in range(len(result)):
        print(result[i][0], end="")
        if i < len(result) - 1:
            print(", ", end="")
        else:
            print()
    dbcursor.close()
    db.close()
