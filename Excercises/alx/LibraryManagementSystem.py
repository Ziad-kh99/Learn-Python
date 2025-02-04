import mysql.connector



db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'P@$$w0rd',
    'database': 'librarydb'
}


db = mysql.connector.connect(
    host = db_config['host'],
    user = db_config['user'],
    password = db_config['password'],
    database = db_config['database']
)


cursor = db.cursor()


# Check if databse exits:
sql = f'''
SHOW DATABASES LIKE '{db_config['database']}'
'''

cursor.execute(sql)
db_exist = cursor.fetchone()


if not db_exist:
    print(f'Database {db_config['database']} doesn\'t exist.\nCreating it...')
    sql = f'''CREATE DATABASE {db_config['database']}'''
    cursor.execute(sql)
    print(f'Database {db_config['database']} created successfully!')
else:
    print(f'Database {db_config['database']} already exists')


sql = '''
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    ISBN VARCHAR(255)
);
'''
cursor.execute(sql)

def add_book():
    title = input('Enter book name: ')
    author = input('Enter book author: ')
    isbn = input('Enter ISBN: ')

    sql = f'''INSERT INTO books(title, author, ISBN) VALUES ('{title}', '{author}', '{isbn}');
'''
    cursor.execute(sql)
    db.commit()
    print(f'{cursor.rowcount} record(s) inserted')

def list_books():
    sql = f'''
SELECT * FROM books;
'''
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def search():
    book_title = input('Search for a book (by title): ')
    sql = f'''
SELECT * FROM books
WHERE title = '{book_title}';
'''
    cursor.execute(sql)
    print(cursor.fetchone())


def delete_book():
    book_id = input('Enter book id to be deleted: ')
    sql = f'''
DELETE FROM books WHERE id = {book_id};
'''
    cursor.execute(sql)
    db.commit()
    print(f'{cursor.rowcount} record(s) deleted!')

add_book()
list_books()
search()
delete_book()

cursor.close()
db.close()




