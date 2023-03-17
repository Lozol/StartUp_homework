import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password='1111'
    )
# 1.Напишіть програму , яка створює нову базу даних 'my_first_db'
my_cursor= my_db.cursor()
my_cursor.execute('CREATE DATABASE my_first_db')

# 2.Напишіть програму, яка створить у базі 'my_first_db'  таблицю 'student' з полями  'id'(INT)і
# 'name'(VARCHAR(255))
mycursor= my_db.cursor()
mycursor.execute('CREATE TABLE my_first_db.student (id INT, name VARCHAR(255))')

# 3.Напишіть програму яка створить у базі 'my_first_db' таблицю 'employee'з полями
# 'id'(INT AUTO_INCREMENT PRIMARY KEY), 'name'(VARCHAR(255)) 'salary'(INT(6))
mycursor_= my_db.cursor()
mycursor_.execute('CREATE TABLE my_first_db.employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),salary INT(6) )')
# 4. Напишіть програму, яка змінює у таблиці'student' поле'id' на PRIMARY KEY
mycursor_1= my_db.cursor()
mycursor_1.execute('ALTER TABLE my_first_db.student ADD PRIMARY KEY (id)')
# 5. Напишіть програму, яка додає до таблиці дані'student' (01,'John'), а до таблиці 'employee'
# -(01,'John',1000)

mycursor_2= my_db.cursor()
mycursor_2.execute('INSERT INTO my_first_db.student (id,name) VALUES (01,"John")')
sql = 'INSERT INTO my_first_db.employee (id,  name, salary) VALUES (%s,%s, %s)'
values = (0o1,'John',1000)
mycursor_2.execute(sql,values)
my_db.commit()
