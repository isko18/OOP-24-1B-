""" БД - База Данных """
""" СУБД - Система управлением базы данных """
""" CRUD - CREATE, RETRIVE, UPDATE, DELETE """

import sqlite3

connect = sqlite3.connect("geeks.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        age INT DEFAULT NULL,
        direction TEXT,
        is_have BOOLEAN NOT NULL DEFAULT FALSE,
        birth_date DATE,
        rating DOUBLE (4,2) DEFAULT (0.0)
    )             
""")

def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    direction = input("Введите направление: ")
    is_have = bool(input("Наличие ноутбука: "))
    birth_date = input("Введите дату рождения: ")
    rating = float(input("Введите свой рейтинг: "))
    
    # cursor.execute(f""" INSERT INTO users
    #                (full_name, age, direction, is_have, birth_date, rating)
    #                VALUES ('{full_name}', {age}, '{direction}', {is_have}, '{birth_date}',
    #                {rating})""")
    
    # connect.commit()
    
    #Использование форматированных строк (f"") для вставки значений в SQL-запрос может привести к уязвимости типа SQL-инъекция, если пользователь вводит специальные символы в текстовые поля.
    
    cursor.execute(""" INSERT INTO users
                   (full_name, age, direction, is_have, birth_date, rating)
                   VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, direction, is_have, birth_date, rating))
    
    connect.commit()
    
    '''Плейсхолдер (англ. placeholder) — это специальный символ или текстовый маркер, который используется в SQL-запросах и других контекстах программирования для обозначения места, куда позже будет вставлено значение'''

def all_students():
    cursor.execute("SELECT * FROM users")
    students = cursor.fetchall()
    print(students)
    
    
def delete_students(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    connect.commit()
    print(f"Пользователь {id}, был успешно удален!")
    
# register()
all_students()
# delete_students(1)


# INTEGER - int
# VARCHAR - str - (Строки с ограничением )
# TEXT - str - (без ограничения)
# BOOLEAN - bool 
# DOUBLE - float 
# NOT NULL - (поле не должен быть  пустым)
# DEFAULT - (по умолчанию)
# id INTEGER PRIMARY KEY AUTOINCREMENT - (PRIMARY KEY - уникальное значение AUTOINCREMENT - авто добавление нумерации)