import pandas as pd
from tabulate import tabulate
import csv
import os
class EmployeeManager:
    emp=[]
    filename = "employees_data.csv"

    def __init__(self):## to load file
        self.load_from_csv()

    def load_from_csv(self):
        ##Load employee data from CSV if file exists.
        if os.path.exists(self.filename):
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                self.emp = list(reader)
                # Convert salary to float
                for e in self.emp:
                    e['Salary'] = float(e['Salary'])
        else:
            self.emp = []
    def save_to_csv(self):
        ##Save current employee list to CSV."""
        with open(self.filename, mode="w", newline="") as file:
            fieldnames = ["ID", "Name", "Position", "Salary", "Email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for e in self.emp:
                writer.writerow(e)
      
    def check_email(self,Email):## check if email exist or not and contain @gmail.com not
         while True:
            if "@gmail.com" not in Email:
                print("Invalid Email: Must contain @gmail.com")
            elif any(Email == em['Email'] for em in self.emp):
                print("Email already exists.")
            else:
                return Email
            Email = input("Enter a valid E@mail address: ")


    def Check_id_exist_or_not(self, ID):
        while any(ID == emp['ID'] for emp in self.emp):
            print("ID already exists.")
            ID = input("Enter a unique Employee_ID: ")
        return ID

    def search_id(self,id): ## delete,search ,update
        for em in self.emp:
            if id == em['ID']:
                return em
        return None
    
    def add_employee(self):
        ID=input('Enter Employee_ID')
        Checked_ID=self.Check_id_exist_or_not(ID)## check if id exist or not
        if  Checked_ID is not None:## if not exist
            ID=Checked_ID

        Name=input('Enter Employee_name')
        Position= input('Enter Employee_position')

        while True:## validate salary
            try:
                Salary= float(input('Enter Employee_salary'))
                break
            except:
                print("Enter valid salary")
 
        Email= input('Enter Employee_email')
        Email=self.check_email(Email)## check if mail exist or not and check if it contain @gmail or not
             
        employee = {
                "ID": ID,
                "Name": Name,
                "Position": Position,
                "Salary": Salary,
                "Email":Email
            }
        self.emp.append(employee)
        self.save_to_csv()
#######################################################################################################################
    def view_employees(self):
        pd.set_option('display.max_rows', None)  
        df = pd.DataFrame(self.emp)
        print("\n=== Employee Table ===")
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
#####################################################################################################################  

    def update(self):
        emp_id = input("Enter the Employee ID to update: ")
        em = self.search_id(emp_id)  # check if id exist or not 
    
        if em is None:## if not found
            print("ID does not exist")
        else:
            new_position = input("New position: ").strip()
            if new_position:
                em['Position'] = new_position
    
            while True:
                try:
                    new_salary = float(input("Enter Employee salary: "))
                    em['Salary'] = new_salary
                    break
                except:
                    print("Enter valid salary")
    
            new_email = input("New email: ").strip()
            if new_email:
                new_email = self.check_email(new_email)
                em['Email'] = new_email
            self.save_to_csv()             
 #######################################################################################################################                                      
    def delete(self):
        emp_id = input("Enter the Employee ID to delete: ")
        employee=self.search_id(emp_id) ## check id exist or not
        if employee is not None: ## if not found
            self.emp.remove(employee)
            self.save_to_csv()
        elif employee is None:
            print('id not exist')
###########################################################################################################################    
    def search_employee(self):
        emp_id = input("Enter the Employee ID you want: ")
        employee=self.search_id(emp_id) ## check id exist or not
        if employee is not None:## if not found
            print(employee)
        elif employee is None:
            print('id not exist')
 ###########################################################################################################################        
         
    def main_menu(self):
        print("Press a to add employee")
        print("Press d to delete employee")
        print("Press u to update employee")
        print("Press v to view all employees")
        print("Press s to search")
        print("Press e to exit")

       

        while True:
             option=input("Select one of these inputs(a,d,u,v,s,e)").lower()
             if(option=='a'):
                    self. add_employee()
             elif (option=='d'):
                    self.delete()
             elif(option=='u'):
                    self.update()
             elif(option=='v'):
                    self.view_employees()
             elif(option=='s'):
                    self.search_employee()
             elif(option=='e'):
                    break
             else:
                    print("invalid input")
                    
            


