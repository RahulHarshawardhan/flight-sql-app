import mysql.connector
# connect to the database server
try:
    conn = mysql.connector.connect(host='127.0.0.1', user='root', password = 'rahul', database='indigo')
    mycursor = conn.cursor()
    print('connection established')
except:
    print('connection Error')

# Create a database on db server.

#mycursor.execute("CREATE DATABASE indigo") # This is to create a database in mysql
#conn.commit()


#create a table.
#airport-> airport_id/code/name/city

#mycursor.execute("""
#CREATE TABLE airport(
 #   airport_id INTEGER PRIMARY KEY,
 #   code VARCHAR(10) NOT NULL,
 #   city VARCHAR(50) NOT NULL,
 #   name VARCHAR(255) NOT NULL
  #  )
#""")

#conn.commit()

#insert data to the table
#mycursor.execute("""
#    INSERT INTO airport value
#    (1, 'DEL','NEW DELHI', 'IGIA'),
 #   (2, 'CCU','kolkata','NSCA'),
#    (3, 'BOM','Mumbai','CSMA')
#""")
#conn.commit()

# search/Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

#update function

mycursor.execute("""
UPDATE airport
SET city= 'Bombay'
WHERE airport_id = 3
""")

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

# Delete operation

mycursor.execute("DELETE FROM airport WHERE airport_id=3")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)
