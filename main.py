import pymysql
from contextlib import contextmanager
from faker import Faker
import random


@contextmanager
def create_connection():

    try:
        connection = pymysql.connect(
            host='localhost', database="hw", user="root", password="password")
        yield (connection)
    except pymysql.Error as error:
        connection.rollback()
        print(error)
    finally:
        connection.close()


def create_table(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
    except pymysql.Error as error:
        connection.rollback()
        print(error)
    finally:
        cursor.close()


if __name__ == "__main__":

    subjects = ["math", "physics", "chemistry", "English", "history"]

    fake = Faker()

    create_groups_table_query = "CREATE TABLE IF NOT EXISTS class(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20));"
    add_groups_query = "INSERT INTO class(name) VALUES (%s);"

    create_teachers_table_query = "CREATE TABLE IF NOT EXISTS teachers(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50));"
    add_teachers_query = "INSERT INTO teachers(name) VALUES (%s);"

    create_students_table_query = "CREATE TABLE IF NOT EXISTS students(id INT PRIMARY KEY AUTO_INCREMENT, student VARCHAR(50), groups_id INT, FOREIGN KEY (groups_id) REFERENCES class(id));"
    add_students_query = "INSERT INTO students(student, groups_id) VALUES (%s, %s);"

    create_subjects_table_query = "CREATE TABLE IF NOT EXISTS subjects(id INT PRIMARY KEY AUTO_INCREMENT, subject VARCHAR(20), teacher_id INT, FOREIGN KEY (teacher_id) REFERENCES teachers(id));"
    add_subjects_query = "INSERT INTO subjects(subject, teacher_id) VALUES (%s, %s);"

    create_marks_table_query = "CREATE TABLE IF NOT EXISTS marks(id INT PRIMARY KEY AUTO_INCREMENT, mark INT, day DATE, student_id INT, subject_id INT, FOREIGN KEY (student_id) REFERENCES students(id), FOREIGN KEY (subject_id) REFERENCES subjects(id));"
    add_mark_query = "INSERT INTO marks(mark, day, student_id, subject_id) VALUES (%s, %s, %s, %s);"

    with create_connection() as connection:

        connection.autocommit(True)

        create_table(connection, create_groups_table_query)
        create_table(connection, create_teachers_table_query)
        create_table(connection, create_students_table_query)
        create_table(connection, create_subjects_table_query)
        create_table(connection, create_marks_table_query)

        # create groups
        for i in range(1, 4):

            cursor = connection.cursor()

            print(f'{i}')

            cursor.execute(add_groups_query, (f'group {i}'))

        # create teachers
        for i in range(5):

            teacher = fake.name()

            print("t" + teacher)

            cursor.execute(add_teachers_query, (teacher))

        # create students
        for i in range(40):
            cursor = connection.cursor()

            student, user_id = fake.name(), random.randint(1, 3)

            print(student, user_id)

            cursor.execute(add_students_query, (student, user_id))

        # create subjects
        for i in subjects:

            cursor, teacher_id = connection.cursor(), random.randint(1, 5)

            print(f"connection {teacher_id}")

            cursor.execute(add_subjects_query, (i, teacher_id))

        # create mark
        for stud in range(1, 41):

            for i in range(20):

                cursor = connection.cursor()

                day, subject_id = fake.date(), random.randint(1, 5)

                student_id = stud

                mark = random.randint(1,5)
                
                print(mark, day, student_id, subject_id)

                cursor.execute(add_mark_query, (mark, day, student_id, subject_id))

        cursor.close()
        
