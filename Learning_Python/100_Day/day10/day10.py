# Function with output
def  my_function():
    result = 3 * 2
    return result

# make our function with output example

first_name = input("Inpur your first name : ")
last_name = input("Input your last name : ")

def format_name(f_name, l_name):
    """_summary_

    Args:
        f_name (_type_): _description_
        l_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    # The crazy is, the documentation below is written automatically
    
    if f_name == "" or l_name == "":
        return "You didnt input your name"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"
    # we cant add something after return, cause return is end of function

print(format_name(first_name, last_name))