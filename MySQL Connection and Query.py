"""mysql -u root -p
Enter password: <enter password>
mysql>GRANT ALL ON *.* to root@'172.25.20.14' IDENTIFIED BY 'put-your-password';
mysql>FLUSH PRIVILEGES;
mysql>exit"""


import pymysql
try:
    conn = pymysql.connect("172.25.20.12","test","test","testdb");
    cursor = conn.cursor()
    #create = """CREATE TABLE EMPLOYEE ( FIRST_NAME  CHAR(20) NOT NULL, LAST_NAME  CHAR(20), AGE INT, SEX CHAR(1), INCOME FLOAT, PRIMARY KEY (FIRST_NAME, LAST_NAME))"""
    #insert = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Aditya', 'Mathpal', 5, 'M', 20000)"""
    #delete = """DELETE FROM EMPLOYEE WHERE FIRST_NAME='Aditya'"""
    #drop = """DROP TABLE EMPLOYEE"""

    #cursor.execute(create)
    #cursor.execute(insert)
    #cursor.execute(delete)
    #cursor.execute(drop)
    conn.commit()   # Note Without commit update will not reflect in the Database. so its compelsory to commit after any change, creation.
    print("Table Created/Updated/Deleted Successfully")

except pymysql.err.DatabaseError as e:
    print("There is an Error",e)

finally:
    cursor.execute("SELECT * FROM EMPLOYEE")
    results = cursor.fetchall()
    print(results)
    cursor.close()
    conn.close()



