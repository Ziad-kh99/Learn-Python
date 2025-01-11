'''
Variable Socpe in python follow the LEGB role:
L: Local
E: Enclosing
G: Global
B: Built-in

python follow the same order to search for variable names L -> E -> G -> B.
'''

x = 'global x'                  # global scope

def outer_fun():
    y = 'local-inclosing y'     # local for outer_fun and enclosing for inner_fun
    x = 'local x'               # local scope
    print (y, x)               

    def inner_fun():
        y = 'local y'           # local scope
        print(y)

    inner_fun()

outer_fun()


#> Explicitly change the global variables inside local scope using 'global' keyword.
global_var = 'global var'

def change_global_var():
    global global_var       # to manibulate the global_var.
    global_var = 'not global var yet'


change_global_var()         # to apply the changes of global_var
print(global_var)


#> Explicitly change the enclosing variables using 'nonlocal' keyword.
def outer():
    a = 'outer a'

    def inner():
        nonlocal a          # to explicitly change local-enclosing variable
        a = 'inner a'
        print(a)
    
    inner()
    print(a)

outer()


#> Prameters ara local scope variables:

def param_var(z):       # z is a local variable for param_var function.
    print(z)    

param_var(9)