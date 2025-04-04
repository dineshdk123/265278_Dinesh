from Management import Employee, Department, save_to_json, load_from_json

# -----------------------
# Sample Main Execution
# -----------------------

data_strings = [
    "Alice,30,Female,E101,HR,48000",
    "Bob,28,Male,E102,IT,55000",
    "Charlie,35,Male,E103,HR,60000",
    "Diana,26,Female,E104,IT,47000",
    "Evan,40,Male,E105,Finance,53000"
]

# Create Employee objects
employees = [Employee.from_string(s) for s in data_strings]

# Create Departments and assign employees
departments = {}
for emp in employees:
    if emp.department not in departments: # getattr(emp, 'department')
        departments[emp.department] = Department(emp.department)
    departments[emp.department].add_employee(emp)

# Print Details
Employee.bonus_policy()
print("\nEmployee Details:")
for emp in employees:
    print(emp.get_details())

def get_average_salary(employees):
    total_salary = sum(emp.salary for emp in employees)
    return total_salary / len(employees) if employees else 0
print('-'*100)

# Calculate and print the average salary of all employees
average_salary = get_average_salary(employees)
print(f"\nAverage Salary of All Employees: ₹{average_salary:.2f}")
print('-'*100)


# Save Data
save_to_json(employees)

# Load and verify
print("\n📂 Loaded Data from JSON:")
loaded_emps = load_from_json() # Should take data from json, create employee objects and return the list 
                               # loaded_emps should look like employees created before
for emp in loaded_emps:
    print(emp.get_details())