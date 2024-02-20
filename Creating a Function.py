''' 
Basic syntax of defining a function:
    def function_name(parameters):
        // what the function does //

function_name()  --> Used to call a function
'''

# Example 1 - By defining parameters in function itself
def print_sum(a, b):
    print(a + b)

a = float(input("Enter any number to add: "))
b = float(input("Enter any number to add: "))
print_sum(a, b)

# Example 2 - By not defining parameters in fucntion itself
def print_sum():
    a = float(input("Enter any number to add: "))
    b = float(input("Enter any number to add: "))
    print(a-b)

print_sum()