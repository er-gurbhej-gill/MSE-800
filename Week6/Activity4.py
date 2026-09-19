class Employee:
    def __init__(self):
        self.name = input("Enter employee name: ")
        self.logged_in = input("Are you logged in? (yes/no): ").lower()
        self.salary = input("Enter salary: ")
        self.email = input("Enter email: ")

def login_required(func):
    def wrapper(employee):
        if employee.logged_in == "yes":
            func(employee)
        else:
            print("Access Denied")
    return wrapper

@login_required
def view_salary(employee):
    print("Salary:", employee.salary)

@login_required
def view_personal_details(employee):
    print("Name:", employee.name)
    print("Email:", employee.email)
    
@login_required
def download_report(employee):
    print("Report downloaded")

if __name__ == "__main__":
    employee = Employee()
    view_salary(employee)
    view_personal_details(employee)
    download_report(employee)