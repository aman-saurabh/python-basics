"""
As we know the concept of OOP revolves around 'objects' and to create an object we need class fo that object
As the class works as the frame for any object. Using a class we can create any number of objects of that class
which all have same properties(i.e attributes or variables) and behaviours(i.e operations or methods),
However properties values can be different based on the parameters we pass in the constructor function.
In Python, a class constructor is a special member function of that class, that is executed whenever
we create a new object of that class.In python we define constructor function using built-in "__init__()" method.
In Python, class constructors doesn't return anything and every class constructor must have at least one argument 'self'
which represents current instance of the class or the current object and apart from that
it can have other arguments also, which are basically used to set the initial value of properties(attributes)
of that object while creating the object.
In Python, we can create a class with the help of 'class' keyword as follows :
"class ClassName: "
# Note :- Here we have used pascal casing for class name. By convention class name should start with capital letter and
first letter of every word in the class name must be capitalize. Such type of naming standard is known as PascalCase
or UpperCaseCamelCase.
A class can have two types of attributes :
1.) class attribute :- It is the part of the class itself and not of a particular object. Hence every object of the
class will have these attributes with same value as defined in the class(i.e it is similar to static variables of Java).
2.) instance attribute :- It is the part of a particular object of the class and not the class itself i.e
every object of the class will have these attributes but value of these attributes in every object might be different
and should be set using initializer parameter while creating the object i.e instance attributes are defined inside
initializer (i.e "__init__(self)" function) of the class.
In a class, both types of attributes are optional. A class can have any number of class attributes as well as
instance attributes. A class can also have any number of operations or methods.
Let's check the syntax of a class with class attributes and instance attributes :
"""
class ClassName:
    # Class attributes
    class_attr1 = "val1"
    class_attr2 = "val2"

    def __init__(self, attr_val1, attr_val2):
        # Here 'self' denotes current objects.
        # Instance attributes
        self.instance_attr1 = attr_val1
        self.instance_attr2 = attr_val2
        # Here we have used different names for initializer parameters (i.e 'attr_val1' and 'attr_val2') and
        # instance attributes(i.e instance_attr1 and instance_attr2).We did it intentionally to show their uses.
        # By convention both should be same.

# Creating object from the class :- 2 ways
# Method 1 :- Using initializer parameters
objA = ClassName(attr_val1=7, attr_val2=9)
# Note that here we are using initializer parameter names and not the instance attributes name.
# i.e initializer parameters are used to pass values while creating the object.

# Method 2 :- Without using initializer parameters
objB = ClassName(1, 5)

# Accessing class attributes and instance attributes
print(objA.class_attr1)
print(objA.instance_attr1)
print(ClassName.class_attr1)
# print(ClassName.instance_attr1)
# Above line will throw error since we can access 'class attributes' using class reference as well as object reference.
# But we can't access instance attribute using class reference. We can access them using object reference only.
# As instance attributes belongs to a particular object and not the class itself.

# Modifying instance attribute
objA.instance_attr2 = 111
print(objA.instance_attr2)
print(objB.instance_attr2)
# So from here it is clear that when we update an instance attribute of one object.
# Value of that attribute in other object doesn't get updated.

# Modifying class attribute using object reference
objA.class_attr2 = "new_val1"
print(objA.class_attr2)
print(objB.class_attr2)
print(ClassName.class_attr2)
# So from here it is clear that when we update a class attribute using object reference of any object.
# Then the value of the class attribute is updated for that particular object only and not for any other object
# and nor for the class.

# Modifying class attribute using class reference
ClassName.class_attr2 = "new_val2"
print(objA.class_attr2)
print(objB.class_attr2)
print(ClassName.class_attr2)
# So from here it is clear that if we update a class attribute using class reference. Then the value is updated
# for the class as well as all objects of that class except those objects, whose that class attribute value,
# we have updated earlier using object reference (i.e "objA.class_attr2" value will still be 'new_val1' and won't be
# updated to 'new_val2' but "objB.class_attr2" and "ClassName.class_attr2" value will be updated to 'new_val2').

"""
So you can use object reference to modify the value of a class attribute if you want to modify the value only 
for that particular object.But in real programs for such requirements we use instance attributes and not the
class attributes.So in real programs, to update the class attributes, preferably we should use class reference. 
"""