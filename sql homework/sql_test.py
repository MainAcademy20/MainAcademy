import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE students
                  (surname text, name text, age int)
               """)

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO students
                  VALUES ('Flex', 'Ivan', '23')"""
               )

# Сохраняем изменения
conn.commit()

# Вставляем множество данных в таблицу используя безопасный метод "?"
students = [('Rex', 'Andy', '24'),
            ('Bex', 'Olga', '25'),
            ('Flex', 'Alex', '18'),
            ('Mex', 'Peter', '412')]

cursor.executemany("INSERT INTO students VALUES (?,?,?)", students)
conn.commit()

sql = "SELECT * FROM students WHERE surname=?"
cursor.execute(sql, ["Bex"])
print(cursor.fetchall())  # or use fetchone()

print("Listing of all the records in the table:")
for row in cursor.execute("SELECT rowid, * FROM students ORDER BY surname"):
    print(row)

print("LIKE query:")
sql = "SELECT * FROM students WHERE surname LIKE 'Fl%'"
cursor.execute(sql)

print(cursor.fetchall())
