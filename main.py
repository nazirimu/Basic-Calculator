from art import logo

def add(n1,n2):
    ''' Adds the two inputs together and returns the sum'''
    return n1 + n2

def subtract(n1,n2):
    ''' subtracts the two inputs together and returns the result'''
    return n1 - n2

def multiply (n1, n2):
    ''' multiplies the two inputs together and returns the result'''
    return n1 * n2

def divide (n1, n2):
    ''' divides the two inputs together and returns the result'''
    return n1 / n2 

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}
def calculator ():
    print(logo)
    number1=float(input("Enter a number: "))
    repeat = True
    flag = False
    while repeat: 
        if flag == True:
            number1 = result
        for operation in operations:
            print(operation)
        choice = input("Enter the operator: ")
        number2= float(input("Enter a number: "))

        function = operations[choice]
        result = function(number1, number2)
        print(f"{number1} {choice} {number2} = {result}")
        should_continue = input(f"Type 'y' to countinue with {result}. Type 'n' to start a new one: ").lower()
        if should_continue == 'n':
            repeat = False
            calculator()
        else:
            flag = True
    
calculator()

