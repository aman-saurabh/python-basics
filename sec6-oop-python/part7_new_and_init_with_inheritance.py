class ParentClass:
    def __new__(cls, name):
        print("Parent class new() method called")
        instance = super(ParentClass, cls).__new__(cls)
        # Note :- Here we are calling 'new()' method of it's parent class i.e base class 'object' class,
        # which requires only one parameter - 'cls'
        return  instance

    def __init__(self, name):
        self.name = name
        print("Parent class init() method called")

class ChildClass(ParentClass):
    def __new__(cls, name):
        print("Child class new() method called")
        instance = super(ChildClass, cls).__new__(cls, name)
        # Note :- Here we are calling 'new()' method of it's parent class i.e ParentClass,
        # which requires two one parameter - 'cls' and 'name'.
        return instance

    def __init__(self, name):
        ParentClass.__init__(self, name)
        # Note :- Here we are calling ParentClass init() method and passing required arguments i.e 'self' and 'name'
        print("Child class init() method called")

parent_obj = ParentClass("Aman")
print("Parent class object name : ", parent_obj.name)
print("")           # Just to give space between results of ParentClass and ChildCLass

child_obj = ChildClass("Saurabh")
print("Child class object name : ", child_obj.name)
