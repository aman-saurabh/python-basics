"""
A variable is only available inside the region it is declared.
It is called scope of the variable.
Based on the region it is declared, a variable can have two types of scopes :
1.) Local scope
2.) Global scope
Local Scope :-
A variable created inside a function belongs to the local scope of that function and is accessible and can be modified
from inside that function only.If we try to access or modify such variables from outside of that function,
it will throw error as it is available only inside the function and outside that function it has no existence.
"""

def local_scope_demo():
    x = 100
    print(x)

local_scope_demo()
# print(x)
# Above line will throw error hence commented.As 'x' is available inside the function 'local_scope_demo' only.

