import mysql.connector
from mysql.connector import Error
# connecting to my mysql
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='cafe',
                                         user='root',
                                         password='password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
print('Welcome to Bushras cafe')


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='cafe',
                                         user='root',
                                         password='password')
    mySql_Create_Table_Query = """CREATE TABLE products (
                             Product_name varchar(250) NOT NULL,
                             Product_ID int(11) NOT NULL AUTO_INCREMENT,
                             Price float NOT NULL,
                             PRIMARY KEY (Product_ID)) """
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Transcations Table created successfully ")
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
