"""
In Python, any script file(i.e ".py" file) is known as module(similar to javascript).
And package is a collection of several such modules.
In python we can use functionality of any module into some other module by importing them as follows :
"from random import shuffle" - Here we are importing "shuffle" function of "random" module.
Sometimes packages are also known as libraries.So far we have used python libraries that comes built-in with Python.
Such libraries are known as standard libraries or build-in libraries.
But in Python we can use other libraries also which don't come built-in with Python.
Actually members of the very large Python community build such libraries and open-source them for fellow developers.
PyPI is a repository for such open-source third party Python packages. It is similar to NPM for node.js.
And we can use such third party libraries in out project by installing them in the project using following command :
"pip install package_name" - Here replace "package_name" with the actual package
you want to install and use in your project.
We will see all these with examples in details.
But first let's see how to create a custom module and use its functionality in some other module.
For this purpose we will create a "my_custom_module.py" file and will create a function in that file.
And we will import that function in this file and call that.
"""

from part2_my_custom_module import my_func

# Calling "my_func" of "part2_my_custom_module.py" file
my_func()

