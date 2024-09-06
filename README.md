# Employee Management System

## Overview
The **Employee Management System** is a Python-based application that allows users to manage employee records using a MySQL database. The system is designed with a focus on CRUD (Create, Read, Update, Delete) operations, providing a user-friendly interface through the `customtkinter` library. This project is ideal for those who want to understand the basics of database management and UI design with Python.

## Features
- **Login Page**: A simple login interface (hardcoded user, no signup).
- **Add Employee**: Add new employee details to the database.
- **Update Employee**: Modify existing employee records.
- **Delete Employee**: Remove an employee's record or delete the entire table.
- **Search Employee**: Find employees based on specific column values.
- **Error Handling**: Displays errors for invalid entries, incomplete data, and invalid search queries.

## Technologies Used
- **Python**: Core programming language.
- **MySQL**: Database management system.
- **customtkinter**: For creating the graphical user interface (GUI).
- **pymysql**: Python library to connect to MySQL databases.

## Project Structure
- `login.py`: Contains the main code for the login page of the Employee Management System.
- `ems.py`: Contains the main code for the interface of management system and logics for CRUD and search operations.
- `database.py`: Contains the database configuration and connection details with SQL queries.
- `requirements.txt`: List of Python dependencies.

## Installation and Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/employee-management-system.git
