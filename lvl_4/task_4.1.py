# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)


# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4


import sqlite3

def get_connection():
    connection = sqlite3.connect("teatchers.db")
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def create_students():
    try:
        connection = get_connection()
        cursor = connection.execute("create table if not exists Students(Student_Id Integer, Student_Name Text, School_Id Integer Primary key); ")
        records = cursor.fetchone()
        connection.commit()

        sql_query = """insert into Students(student_id, student_name, school_id)
                        values (201, 'Иван', 1),
                        (202, 'Петр', 2),
                        (203, 'Анастасия', 3),
                        (204, 'Игорь', 4);"""

        cursor = connection.execute(sql_query)
        records = cursor.fetchone()
        connection.commit()

        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка в получении данных:", error)


#create_students()


# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

def get_student(student_id):
    try:
        connection = get_connection()
        sql_query = """select student_id, student_name, Students.school_id, school_name
                        from Students
                        join School on Students.school_id=School.school_id
                        where student_id=?;"""

        cursor = connection.execute(sql_query,(student_id,))
        records = cursor.fetchone()
        if records==None:
            print("Нет студента с ID ", student_id)
        else:
            print('ID Студента:', records[0])
            print('Имя студента:', records[1])
            print('ID школы:', records[2])
            print('Название школы:', records[3])
        

        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка в получении данных:", error) 

get_student(202)