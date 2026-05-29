Employee Management System

Description

The Employee Management System is a desktop application built using Python and Tkinter.
It allows users to manage employee records with CRUD (Create, Read, Update, Delete) operations.
The system is connected to a MySQL database for persistent data storage.



Features

* Login system (hardcoded credentials)
* Add new employee records
* View all employees
* Search employee by name or ID
* Update employee details
* Delete employee records
* Data stored in MySQL database
* User-friendly GUI using Tkinter

Tech Stack

Programming Language:Python
GUI Framework:Tkinter
Database:MySQL

Installation
1. Clone the repository
git clone https:https://github.com/Jayesh5553/Employee-Management-System-
cd employee-management-system


2. Install dependencies
pip install mysql-connector-python

3.Setup MySQL Database

Create a database and table:


CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100),
    salary FLOAT
);


 Login Credentials

(Hardcoded for demo purposes)

Username:admin
Password:admin123

Usage
Run the application:
python main.py

Login using the provided credentials
Perform CRUD operations and search employees

Screenshots

(Add screenshots of your GUI here)


Limitations

Login system uses hardcoded credentials (not secure)
No role-based access control

Future Improvements

Implement database-based authentication
Add password hashing
Improve UI design
Add employee sorting and filtering

Author
GitHub: https://github.com/your-username

