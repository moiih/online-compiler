import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        database = 'mydb',
        user = 'root',
        password = 'muskan6023',
        auth_plugin = 'mysql_native_password'
    )

    cursor = connection.cursor()
    cursor.execute('select * from school')
    records = cursor.fetchall()
    print("Total number of rows in school is", cursor.rowcount )

    print("\nPrinting Each Student Record:\n")
    for row in records:
        print("Name =", row[0] )
        print("\tClass =", row[1] )
        print("\tSection =", row[2] )
        print("\tRoll no. =", row[3] )

except Error as e:
    print("Error reading data from MySQL table --->",e)

finally:
    if( connection.is_connected() ):
        connection.close()
        cursor.close()
        print("MySQL Connection is closed")











