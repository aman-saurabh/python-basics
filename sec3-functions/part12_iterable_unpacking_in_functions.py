employee_work_hours = [("Aman", 100), ("Mohit", 120), ("Rohan", 85), ("Sumit", 110)]

def get_best_employee(employees_details):
    work_hour = 0
    emp_name = ""

    for employee, hour in employees_details:
        if hour > work_hour:
            work_hour = hour
            emp_name = employee
        else:
            pass

    return emp_name, work_hour
# Note :- Here we are returning a tuple, but in such cases encapsulating it in parenthesis is not required
# and even not recommended.i.e if we return multiple values and don't apply any bracket it will return data as tuple.

best_emp = get_best_employee(employee_work_hours)
print("Returned data type : ", type(best_emp))
print("Best employee name : ", best_emp[0])
print("Best employee's total work hour : ", best_emp[1])

# Note :- Here since the function is returning a tuple.
# So we can directly catch the values in same number of variables
# as the element in the tuple using the concept of iterable unpacking as follows :

best_emp_name, best_emp_work_hour = get_best_employee(employee_work_hours)

print("Best employee name : ", best_emp_name)
print("Best employee's total work hour : ", best_emp_work_hour)