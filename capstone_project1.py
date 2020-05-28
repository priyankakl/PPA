import sqlite3
import os
import smtplib  
from tabulate import tabulate


conn = sqlite3.connect('Employee_Directory.db')
curr = conn.cursor()

class Employee:

    def create_employees_table():
        """
        This function is used to create table
        """
        curr.execute(
            "CREATE TABLE IF NOT EXISTS employees(e_id INTEGER, e_name TEXT, e_gender TEXT, e_email TEXT, e_phone INTEGER, e_dateOfJoinning DATE)")


    def employee_data_entry():
        """
        This function is used to enter employee data into the table by getting the input values from the user
        """
        e_name = ''
        e_gender = ''
        e_email = ''
        e_phone = 0
        e_dateOfJoinning = ''
        e_id = int(input("Enter Employee ID: "))
        
        e_name = input("Enter Employee Name: ")

        e_gender = input("Enter Gender: ")

        e_email = input("Email: ")
        

        e_phone = int(input("Phone: "))
        if len(str(e_phone)) != 10:
            print("invalid input")

        e_dateOfJoinning = input("Date Of Enrollment (yyyy-mm-dd) ")
        
        curr.execute("INSERT INTO employees VALUES(?,?,?,?,?,?)", (e_id, e_name, e_gender, e_email, e_phone, e_dateOfJoinning))
        conn.commit()
        print('Data Inserted Successfully')


    def viewAllEmployees():
        """
        This is used to view all the employees. It takes input from user to confirm if he/she wants 
        to see full details of an employee
        """
        curr.execute("SELECT e_id ,e_name,e_email FROM employees")
        conn.commit()
        employees = curr.fetchall()
        print("\nEMPLOYEES ARE:")
        print("ID    NAME            Email")
        print(tabulate(employees))
        # for employee in employees:
        #     print(employee[0], ' - ', employee[1], ' - ', employee[2])
        avlEmployeeId = [int(i[0]) for i in employees]
        print('\n \nEnter Employee Id For Details')
        print('Or Enter 0 to go back')
        e_idChoice = int(input())
        if e_idChoice == 0:
            return
        elif e_idChoice in avlEmployeeId:
            Employee.view_employee_detail(e_idChoice)
        else:
            print('CHOOSE CORRECT OPTION \n')
            Employee.viewAllEmployees()


    def del_employee(eid):
        """
        This function is used to delete the employee with the help of eid(employee id)
        """
        curr.execute("DELETE FROM employees WHERE e_id=:e_id", {"e_id": eid})
        conn.commit()
        print('Employee DELETED SUCCESSFULLY')
        Employee.viewAllEmployees()


    def update_employee(eid):
        """
        This function is used to update employee with the help of eid(employee id)
        """
        curr.execute("SELECT * FROM employees WHERE e_id=:e_id", {"e_id": eid})
        conn.commit()
        employeeDetail = curr.fetchone()

        oeid = employeeDetail[0]
        oename = employeeDetail[1]
        oegender = employeeDetail[2]
        oeemail = employeeDetail[3]
        oephone = employeeDetail[4]
        oedateEnrolled = employeeDetail[5]

        nsname = ''
        nsgender = ''
        nsemail = ''
        nsphone = 0
        nsdateEnrolled = ''
        print('Old Employee Name: ', oename, ' \nEnter New Employee Name: ')
        nsname = input()
        if nsname == '':
            nsname = oename
        
        print('Old Employee Gender: ', oegender, ' \nEnter New Employee Gender: ')
        nsgender = input()
        if nsgender == '':
            nsgender = oegender
            
        print('Old Email: ', oeemail, ' \nEnter New Email: ')
        nsemail = input()
        if nsemail == '':
            nsemail = oeemail

        print('Old Phone: ', oephone, ' \nEnter New Phone: ')
        nsphone = input()
        if nsphone == '':
            nsphone = oephone
        else:
            nsphone = int(nsphone)
        if len(str(nsphone)) != 10:
            print("invalid input")

        print('Old Employee Date Enrolled: ', oedateEnrolled, ' \nEnter New Employee Date Enrolled: ')
        nsdateEnrolled = input()
        if nsdateEnrolled == '':
            nsdateEnrolled = oedateEnrolled

        curr.execute(
            "UPDATE employees SET e_name = :e_name, e_gender = :e_gender, e_email = :e_email,  e_phone = :e_phone, e_dateOfJoinning = :e_dateOfJoinning WHERE employees.e_id = :e_id",
            ({"e_name": nsname, "e_gender": nsgender, "e_email": nsemail, "e_phone": nsphone,
            "e_dateOfJoinning": nsdateEnrolled, "e_id": oeid}))
        conn.commit()

        print('\nEmployee UPDATED SUCCESSFULLY')
        Employee.view_employee_detail(oeid)


    def view_employee_detail(eid):
        """
        This function is used to view all the details of the employee
        """
        curr.execute("SELECT * FROM employees WHERE e_id=:e_id", {"e_id": eid})
        conn.commit()
        employeeDetail = curr.fetchone()
        print('\nEmployee ID: ', employeeDetail[0], '\nEmployee Name: ', employeeDetail[1])
        print('Employee Gender: ', employeeDetail[2])
        print('Email: ', employeeDetail[3])
        print('Phone: ', employeeDetail[4])
        print('Date Of Enrollment: ', employeeDetail[5])
        while True:
            print("========================================================")
            print('\n \n Enter 1 to DELETE the employee')
            print('Enter 2 to EDIT the employee details')
            print('Or Enter 0 to Go back')

            e_idChoice = int(input('Enter: '))

            if e_idChoice == 0:
                return
            if e_idChoice == 1:
                Employee.del_employee(employeeDetail[0]
                            )
            if e_idChoice == 2:
                Employee.update_employee(employeeDetail[0])
            
            else:
                print('\n Enter Correct Choice.')



    def appreciate_employee(e_email):
        """
        This function is used to send email to a specific employee.
        """
        conn =smtplib.SMTP('smtp.gmail.com',587)  
        type(conn)  
        conn.ehlo()  
        conn.starttls()  
        conn.login('hr1company1@gmail.com','priyanka@123')  
        conn.sendmail('hr1company1@gmail.com',e_email,'Subject:Good Job!\n\nHey your work is outstanding! Keep up the good work!')  
        print("\nmail sent successfully!")
        conn.quit() 




