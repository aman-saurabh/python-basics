# Part1 :-
"""
In this program we will see how to create a custom package and how to use them in any other module.
For this purpose we have created a package "MyMainPackage" and inside that package we have created a sub-package
"MySubPackage".We have also created a function in "MySubPackage" to see how to call that function in the "MyMainPackage"
We have created a function in "MyMainPackage" also to see how to call those functions (i.e functions defined in
"MyMainPackage" as well as in "MySubPackage") in a module that exists outside of both packages(i.e in current module).
But before we proceed further notice the "__init__.py" file in "MyMainPackage" as well as in "MySubPackage".
If you open these file you will find they are empty.
Actually this is the file that differentiate between a normal directory and a package.
So in every package there must be an empty "__init__.py" file.
"""
from MyMainPackage import my_main_package_module
from MyMainPackage.MySubPackage import my_sub_package_module

# Calling "my_main_package_module" file's function
my_main_package_module.main_package_func()

# Calling "my_sub_package_module" file's function
my_sub_package_module.sub_package_func()

# Part2 :-
import part4_name_main_relation
# Ideally import statements should be on the top of the file.
# But here we don't want our code to be messed with above code so imported here.
part4_name_main_relation.name_main_func()
