class EmployeeDetails:
    # Class attribute
    company = "Tech Passel"

    # Initializer
    def __init__(self, name, post, location):
        # Instance attributes
        self.name = name
        self.post = post
        self.location = location

    # Operations, Actions or methods
    def display_emp_salary(self):
        salary = 100000 if self.post == 'Manager' else 50000
        print(f"{self.name}'s current salary is Rs. {salary}/-")

    def get_emp_details(self):
        return f"{self.name} works in {EmployeeDetails.company} company as {self.post} in {self.location} office."
        # Note :- Here we can also use "self.company" inplace of "EmployeeDetails.company" as we can access
        # class attributes using class reference as well as object reference.

# Creating object of 'EmployeeDetails'
emp1 = EmployeeDetails("Aman", "Developer", "Noida")

# To access class attributes :
print("Company :", emp1.company)

# To access instance attributes :
print("Name : ", emp1.name)
print("Post : ", emp1.post)
print("Location : ", emp1.location)

# To modify class attribute :
EmployeeDetails.company = "Abc Ltd."
# As we learned in previous part, here we can use object reference also for modifying class attribute but we shouldn't
# use them.As in that case value of class attribute will be modified for that particular object but will remain same
# as earlier for class reference as well as other objects reference of same class. i.e following code will update value
# of class attribute "company" for "emp1" object but not for the class "EmployeeDetails" as well as it's other objects.
emp1.company = "Xyz Ltd."
print(emp1.company)
print(EmployeeDetails.company)

# To modify instance attributes :
emp1.name = "Saurabh"

# To call a function not returning anything
emp1.display_emp_salary()

# To call a function returning some value
emp_details = emp1.get_emp_details()
print(emp_details)


