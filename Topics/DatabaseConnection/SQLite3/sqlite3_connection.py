import sqlite3

db_conn = sqlite3.connect('mydata.db')   # create/connect database.

my_cursor = db_conn.cursor()

sql_statement = '''
create table persons (
    first_name text,
    last_name text,
    age integer
)
'''

# my_cursor.execute(sql_statement)

sql_statement = '''
insert into persons values
('Ziad', 'Khaled', 27),
('Hossam', 'Khaled', 31),
('Aseel', 'Elsayed', 5);
'''
# my_cursor.execute(sql_statement)

sql_statement = '''
select * from persons
where last_name = 'Khaled';
'''

my_cursor.execute(sql_statement)
rows = my_cursor.fetchall()

for row in rows:
    print(row)

db_conn.commit()
my_cursor.close()
db_conn.close()

