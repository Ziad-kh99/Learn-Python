import mysql.connector


# Database Connection:
my_db = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'P@$$w0rd',
    database = 'testdb'
)


# Db Cursor:
my_cursor = my_db.cursor()


# Create a table:
sql = '''CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);'''

my_cursor.execute(sql)

print('Table created successfully!')


# Insert some customers data:
sql = '''
INSERT INTO customers (name, email)
VALUES ('John Doe', 'john.doe@example.com'),
       ('Ziad Khaled', 'ziad.kh@gmail.com');
'''

my_cursor.execute(sql)
my_db.commit()
print(f'{my_cursor.rowcount} record(s) inserted.')


# Read all customer data:
sql = '''
SELECT * FROM customers;
'''
my_cursor.execute(sql)
myresult = my_cursor.fetchall()
print('Customers:')
for row in myresult:
    print(row)


# Update a customer's email:
sql = '''
UPDATE customers SET email = 'ziad.khaled@hotmail.com' 
WHERE id = 2;
'''
my_cursor.execute(sql)
my_db.commit()

print(f'{my_cursor.rowcount} record(s) updated')
      

# Read the updated customers data:
sql = '''SELECT * FROM customers WHERE id = 2;'''
my_cursor.execute(sql)
myresult = my_cursor.fetchone()

print('Updated Customer:')
print(myresult)


# Delete a cutomer:
sql = '''DELETE FROM customers WHERE id = 1;'''
my_cursor.execute(sql)
my_db.commit()

print(f'{my_cursor.rowcount} record(s) deleted')


# Close Connections:
my_cursor.close()
my_db.close()

print('Database connection closed')

