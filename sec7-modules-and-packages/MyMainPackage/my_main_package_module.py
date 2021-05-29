# Note - Here applying below condition is important. Other wise it will throw error in import statement
# in part3_package_uses_demo.py file, since when we import this module anywhere else
# it can't get 'MySubPackage' in that module path and throws 'ModuleNotFoundError' due to path mismatch.
# Hence to avoid such problem we used following condition, which basically tells the compiler -
# Execute if block in case the program in directly run from command line and
# execute else block if the program is imported in some other file.
if __name__ == '__main__':
    from MySubPackage import my_sub_package_module
else:
    from .MySubPackage import my_sub_package_module

# Calling "my_sub_package_module" file's function
my_sub_package_module.sub_package_func()

# Defining a function in "My_main_package_module"
def main_package_func():
    print("Hello, I am defined in my_main_package_module inside MyMainPackage")


# Note :- From here it is clear that path has a important role in modules and packages.
# And Relative path of same module can be different for different cases like here relative path for
# import statement and the current file are different. Hence we need to be careful while using import statements.
# We can also use absolute path inplace of "Relative path" to avoid such possible mistakes.
