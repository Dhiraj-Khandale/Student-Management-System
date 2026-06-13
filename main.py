# Student Management System
# Technologies: Python, SQLite, OOPs

import sqlite3

def create_connection():
    conn = sqlite3.connect("students.db")
    return conn

class Student:
    def __init__(self, name, age, course, marks):
        self.name   = name
        self.age    = age
        self.course = course
        self.marks  = marks

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Course: {self.course} | Marks: {self.marks}")

def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            age    INTEGER,
            course TEXT,
            marks  REAL
        )
    """)
    conn.commit()

def add_student(conn):
    name   = input("Enter Name   : ")
    age    = int(input("Enter Age    : "))
    course = input("Enter Course : ")
    marks  = float(input("Enter Marks  : "))
    student = Student(name, age, course, marks)
    conn.execute(
        "INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
        (student.name, student.age, student.course, student.marks)
    )
    conn.commit()
    print("Student added successfully!")
    input("\nPress Enter to continue...")

import sqlite3

def create_connection():
    conn = sqlite3.connect("students.db")
    return conn

class Student:
    def __init__(self, name, age, course, marks):
        self.name   = name
        self.age    = age
        self.course = course
        self.marks  = marks

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Course: {self.course} | Marks: {self.marks}")

def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            age    INTEGER,
            course TEXT,
            marks  REAL
        )
    """)
    conn.commit()

def add_student(conn):
    name   = input("Enter Name   : ")
    age    = int(input("Enter Age    : "))
    course = input("Enter Course : ")
    marks  = float(input("Enter Marks  : "))
    student = Student(name, age, course, marks)
    conn.execute(
        "INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
        (student.name, student.age, student.course, student.marks)
    )
    conn.commit()
    print("Student added successfully!")
    input("\nPress Enter to continue...")

def view_students(conn):
    cursor = conn.execute("SELECT * FROM students")
    rows   = cursor.fetchall()
    if not rows:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Marks: {row[4]}")
    
    input("\nPress Enter to continue...")

def search_student(conn):
    name   = input("Enter student name to search: ")
    cursor = conn.execute(
        "SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",)
    )
    rows = cursor.fetchall()
    if not rows:
        print("No student found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Marks: {row[4]}")
        input("\nPress Enter to continue...")    

def update_student(conn):
    sid    = int(input("Enter Student ID to update: "))
    marks  = float(input("Enter new Marks: "))
    conn.execute(
        "UPDATE students SET marks = ? WHERE id = ?", (marks, sid)
    )
    conn.commit()
    print("Student updated successfully!")
    input("\nPress Enter to continue...")

def delete_student(conn):
    sid = int(input("Enter Student ID to delete: "))
    conn.execute("DELETE FROM students WHERE id = ?", (sid,))
    conn.commit()
    print("Student deleted successfully!")
    input("\nPress Enter to continue...")

def main():
    conn = create_connection()
    create_table(conn)
    while True:
        print("""
=============================
  Student Management System
=============================
1. Add Student
2. View All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit
=============================""")
        choice = input("Enter your choice: ")
        if   choice == "1": add_student(conn)
        elif choice == "2": view_students(conn)
        elif choice == "3": search_student(conn)
        elif choice == "4": update_student(conn)
        elif choice == "5": delete_student(conn)
        elif choice == "6":
            print("Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

def search_student(conn):
    name   = input("Enter student name to search: ")
    cursor = conn.execute(
        "SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",)
    )
    rows = cursor.fetchall()
    if not rows:
        print("No student found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Marks: {row[4]}")
        input("\nPress Enter to continue...")    

def update_student(conn):
    sid    = int(input("Enter Student ID to update: "))
    marks  = float(input("Enter new Marks: "))
    conn.execute(
        "UPDATE students SET marks = ? WHERE id = ?", (marks, sid)
    )
    conn.commit()
    print("Student updated successfully!")
    input("\nPress Enter to continue...")

def delete_student(conn):
    sid = int(input("Enter Student ID to delete: "))
    conn.execute("DELETE FROM students WHERE id = ?", (sid,))
    conn.commit()
    print("Student deleted successfully!")
    input("\nPress Enter to continue...")

def main():
    conn = create_connection()
    create_table(conn)
    while True:
        print("""
=============================
  Student Management System
=============================
1. Add Student
2. View All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit
=============================""")
        choice = input("Enter your choice: ")
        if   choice == "1": add_student(conn)
        elif choice == "2": view_students(conn)
        elif choice == "3": search_student(conn)
        elif choice == "4": update_student(conn)
        elif choice == "5": delete_student(conn)
        elif choice == "6":
            print("Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()