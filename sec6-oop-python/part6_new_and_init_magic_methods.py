"""
1.) "__new__()" method :- It is the first step of instance creation.It is called first and is responsible for
    returning a new instance of the class.
2.) "__init__()" method :- It doesn't return anything and is only responsible for initialization of the instance
    (or instance attributes).It is called after the instance has been created i.e after "__new__()" method.
# Note :- "__new__()" method is called before the instance creation i.e when it is called instance and hence 'self'
doesn't exist.So it doesn't accept 'self' instead it accept one other required parameter 'cls'.Since in base class
(i.e object class) it is defined with 'cls' parameter.
# Note :- Here 'self' and 'cls' are convention.If you want, you can use some other name also.
"""
# Example of "__new__()" and "__init__()" methods in a custom class:

class CustomClass:

    def __new__(cls, a, b):
        print("new() method called.")
        instance = super(CustomClass, cls).__new__(cls)
        return instance

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f"a = {self.a} & b= {self.b} is initialized by init() method call.")

# Creating CustomClass object.No need to hold in a variable as we are not going to use them further.
CustomClass(1, 3)

