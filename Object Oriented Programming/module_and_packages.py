def display():
    print("Hello World")


def main():
    print("Hello World")
    display()


if __name__ == '__main__':
    main()

"""
    Difference between using if __name__ == '__main__' and not using it ?
    
    If we want to use a Python file both as a script (i.e., running it directly, like python module_and_packages.py) and as a 
    module (importing it and calling functions, e.g., functions.display()), a common issue arises.

    Suppose we have a file called module_and_packages.py with a function named main(). If we call main() directly in module_and_packages.py 
    and then execute python module_and_packages.py, the main() function will run as expected.
    
    However, if we import this file in another script (e.g., import functions), the main() function will also be executed 
    automatically, even if we haven’t explicitly called it.
    
    When we import a module, we don’t expect its code to execute automatically. Instead, we expect only the functions or 
    variables that we explicitly invoke to run. To prevent this unintended behavior, we use the if __name__ == 
    '__main__': construct. It ensures that certain parts of the code are only executed when the file is run as a script, 
    not when it is imported as a module.
"""