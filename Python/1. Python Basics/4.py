# Defining a global variable 'x'
x = 50

def display_variables():
    x = 25  # This 'x' is a local variable inside the function
    print("Local variable x inside function:", x)

# Calling the function to print local x
display_variables()

# Printing the global variable outside of the function
print("Global variable x outside function:", x)

# To modify the global variable within the function, use 'global'
def modify_global():
    global x
    x = 100  # Now this modifies the global x
    print("Global variable x modified inside function:", x)

# Calling the function that modifies the global x
modify_global()

# Printing the global variable again to see the change
print("Global variable x after modification:", x)
