import sqlite3

connection = sqlite3.connect('example_sql.db') # Создание базы данных

# Создание таблицы
connection.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')


# Создание записи
def create_user(name, age):
    connection.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    connection.commit()


# Чтение записи
def read_user(id):
    cursor = connection.execute("SELECT * FROM users WHERE id=?", (id,))
    row = cursor.fetchone()
    return row

# Обновление записи
def update_user(id, name, age):
    connection.execute("UPDATE users SET name=?, age=? WHERE id=?", (name, age, id))
    connection.commit()

# Удаление записи
def delete_user(id):
    connection.execute("DELETE FROM users WHERE id=?", (id,))
    connection.commit()


# Пример использования
create_user("John", 30)
create_user("Jane", 25)

user = read_user(1)
print(user)

update_user(1, "Johnny", 31)

user = read_user(2)
print(user)

#delete_user(1)

user = read_user(3)
print(user)

# Закрытие соединения
connection.close()


connection.close()
