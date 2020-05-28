from capstone_project1 import Employee

def main():
    Employee.create_employees_table()
    while True:
        print("===========================================================")
        print('Enter 1 to add an Employee')
        print('Enter 2 to view all Employees')
        print('Enter 3 to appreciate an Employee')
        print('Enter 0 to Go back')

        choice = int(input('Enter: '))

        if choice == 1:
            try:
                Employee.employee_data_entry()
            except:
                print('Data entry failed. Please Try Again.')
                Employee.employee_data_entry()

        elif choice == 2:
            Employee.viewAllEmployees()
        
        elif choice == 3:
            e_email = input("Enter emailD of the employee:\t")
            Employee.appreciate_employee(e_email)
            
        elif choice == 0:
            return

        else:
            print('PLEASE ENTER A VALID CHOICE \n')
        
main()