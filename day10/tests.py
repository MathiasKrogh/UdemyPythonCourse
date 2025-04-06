#Function with output
def format_name(f_name, l_name):
    """The function returns a formatted version of your first and last name
    e.g. Mathias Krogh
    """
    if f_name == "" or l_name == "":
        return "You didn't provide all inputs"
    full_name = f_name.title() + " " + l_name.title()
    return full_name

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
print(f"Your full name is {format_name(first_name, last_name)}")