import mysql.connector 


my_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@$$w0rd',
    database = 'testdb'
)

my_cursor = my_db.cursor()


#> Create Table:
sql_statement = '''
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    adderss VARCHAR(250),
    email VARCHAR(150)   
    );
'''
# my_cursor.execute(sql_statement)



#> Insert Data:
sql_statement = '''
INSERT INTO employees (first_name, last_name, adderss, email)
VALUES ('Ziad', 'Khaled', 'Aswan-Egypt', 'ziad@gmail.com'),
       ('Hossam', 'Khaled', 'Aswan-Egypt', NULL);
'''

# my_cursor.execute(sql_statement)
# my_db.commit()


#> Query Data:
sql_statement = '''
SELECT * FROM employees;
'''

my_cursor.execute(sql_statement)
result_set = my_cursor.fetchall()

for row in result_set:
    print(row)


#> Modify Data:
sql_statement = '''
UPDATE employees SET email = 'hoss@hotmail.com' 
WHERE first_name = 'Hossam'
'''
# my_cursor.execute(sql_statement)
# my_db.commit()


#> Delete Data:
sql_statement = '''
DELETE FROM employees WHERE emp_id = 5;
'''

# my_cursor.execute(sql_statement)
# my_db.commit()



#> Close db connection:
my_cursor.close()
my_db.close()
