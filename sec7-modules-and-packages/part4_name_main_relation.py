"""
As learned in previous part we can check whether a module is executed directly or
is being executed through some other file using import statements by using (__name__ == '__main__') condition
"""
def name_main_func():
    if __name__ == '__main__':
        print("Print this statement if the file is being executed directly.")
    else:
        print("Print this statement if the file is imported somewhere else.")

# Calling above function if the file is being executed directly from command prompt and not imported anywhere else
if __name__ == '__main__':
    name_main_func()
