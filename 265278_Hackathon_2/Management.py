class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def get_details(self):
        return(f"name:{self.name}\nage:{self.age}\ngender:{self.gender}")

# employee1=Person("Alice",30,"Female")
# employee1.get_details()

#Inheritance Person class
class Employee(Person):
    def __init__(self,name,age,gender,emp_id,department,salary):
        super().__init__(name,age,gender)
        self.emp_id=emp_id
        self.department=department
        self.salary=salary
    
    def get_details(self):
        super().get_details()
        return f"name:{self.name}age:{self.age}gender:{self.gender}emp_id:{self.emp_id}department:{self.department}salary:{self.salary}"

    def is_eligible_for_bonus(self):
        if self.salary<50000:
            return True
        else:
            return False
        
    @classmethod
    def from_string(cls,data_string):
        data = data_string.split(',')
        return cls(data[0], int(data[1]), data[2], data[3], data[4], float(data[5]))
 
    @staticmethod
    def bonus_policy():
        print("\u20B9 Bonus Policy: Employees earning less than 50000 are eligible for a bonus otherwise they won't get bonus from company,any concern means plz conatct HR.")

class Department():
    def __init__(self,name):
        self.name=name
        self.employees=[]

    def add_employee(self,employee):
        self.employees.append(employee)

    def get_average_salary(self):
        if self.employees:
            total_salary=sum(emp.salary for emp in self.employees)
            return total_salary/len(self.employees)
        return 0
    
    def get_all_employees(self):
        return [emp.get_details() for emp in self.employees]

import json

def save_to_json(employees, filename="employees.json"):
    with open(filename, 'w') as file:
        employees_data = [emp.__dict__ for emp in employees]# Convert employee objects to dictionaries (to make them JSON serializable)
        json.dump(employees_data, file, indent=4)
 
# Function to load employee data to Department
def load_from_json(filename="employees.json"):
    with open(filename, 'r') as file:
        employees_data = json.load(file)# Load the employee data from JSON file
        employees = []
       
        for data in employees_data:
            # Recreate Employee objects from the loaded data
            emp = Employee(data['name'], data['age'], data['gender'], data['emp_id'], data['department'], data['salary'])
            employees.append(emp)
       
        return employees    
