import sqlite3
db = sqlite3.connect("Employee.sqlite")
cus = db.cursor()
cus.execute('create table employee_detail(employee_id int primary key, name varchar(100), age int,department varchar (100),salary int)')
db.commit()
cb.close()