import pymysql
from tkinter import messagebox


def connect_database():
    global mycursor, conn
    try:
        conn=pymysql.connect(host='localhost', user='root', password='char@2003')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'Something wnt wrong, Please open mysql app before running again')
        return 0
    
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS employee(Id VARCHAR(5), Name VARCHAR(50), Phone_NO VARCHAR(10), Role VARCHAR(20), Gender VARCHAR(20), Salary DECIMAL(10, 2))')


def insert(id, name, phone, role, gender, salary):
    mycursor.execute('INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)', (id, name, phone, role, gender, salary))
    conn.commit()

def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    mycursor.execute('UPDATE employee SET Name=%s, Phone_No=%s, Role=%s, Gender=%s, Salary=%s WHERE Id=%s', (new_name, new_phone, new_role, new_gender, new_salary, id))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM employee WHERE Id=%s', id)
    conn.commit()

def search(option, value):
    mycursor.execute(f'SELECT * FROM employee WHERE {option} = %s', value)
    result = mycursor.fetchall()
    return result

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM employee WHERE Id=%s', id)
    result =  mycursor.fetchone()
    return result[0] > 0

def fetch_employee():
    mycursor.execute('SELECT * FROM employee')
    result =  mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE employee')
    conn.commit()
connect_database()