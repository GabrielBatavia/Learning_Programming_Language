# make calculator program

from art import logo

# add function 
def add(n1, n2):
    return n1 + n2

# Subtract function
def subtrack(n1, n2):
    return n1 - n2

# multiply function
def multiply(n1, n2):
    return n1 * n2

# divide function
def divide(n1, n2):
    return n1 / n2

# make dictionary for calculations
math_operator = {"+": add,
                 "-": subtrack,
                 "*": multiply,
                 "/": divide,}


def calculator():
    # get input from user for our argument
    num1 = float(input("Whats the first number? : "))
    num2 = float(input("Whats the second number? : "))
        
    for key in math_operator:
        print(key)

    operation_symbol = input("Pick an operation from the line above: ")

    # get choosen operation function and call it 
    choosen_function = math_operator[operation_symbol]
    result = choosen_function(num1, num2)
        
    print(f"{num1} {operation_symbol} {num2} = {result}")

    continue_calculator = True

    while not continue_calculator == False:
        print("Are you want to continue to calculate?") 
        print("yes for continue calculate the previous result")
        print("type restart to restart the calculator") 
        print("no for exit this program")
        user_answer = input("type here : ")
        
        if user_answer == "yes":
                
            num1 = result
                
            choosen_num = (input("Whats the next number? : "))

            operation_symbol = input("Pick an operation from the line above: ")
            
            # get choosen operation function and call it 
            choosen_function = math_operator[operation_symbol]
            result = choosen_function(num1, choosen_num)
            
            print(f"{num1} {operation_symbol} {choosen_num} = {result}")
        
        elif user_answer == "restart":
            calculator()
            continue_calculator = False
        else:
            print("Bye! Thanks for using this calculator")
            exit()



# the main start
print(logo)

calculator()