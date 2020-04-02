# This Program is to explain the scope of a variable
File = "Assignment -1 Global"

def myfunc():
    scope = " Assignment -2 Local to myfunc"
    print("The scope for variable scope is " + scope + " with respect to the function myfunc")
    print("The scope for variable scope is " + scope1 + " with respect to the function myfunc")

def main():
    scope = "Assignment -3 Local to main"
    print("The scope for variable scope is " + scope + " with respect to the function myfunc")
    myfunc()


if __name__ == "__main__":
    print("The scope for variable scope is " + scope1 + " with respect to the function myfunc")
    main()
