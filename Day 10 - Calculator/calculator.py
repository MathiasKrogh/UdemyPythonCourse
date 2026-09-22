from art import logo

print(logo)

#Add the second parameter to the first
def add(n1, n2):
    return n1 + n2

#Subtract the second parameter from the first
def subtract(n1, n2):
    return n1 - n2

#Multiply the first parameter by the second parameter
def multiply(n1, n2):
    return n1 * n2

#Divide the first parameter by the second parameter
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate(n1, char, n2):
    calc_function = operations[char]
    answer = calc_function(n1, n2)
    print(f"{n1} {char} {n2} = {answer}")
    return answer

end = False

def get_end():
    return end

def set_end(state):
    global end
    end = state
    return end

def calculator():
    number1 = float(input("What's the first number? "))
    end = get_end()
    while not end:
        for char in operations:
            print(char)
        char = input("Pick an operation from the lines above: ")
        number2 = float(input("What's the second number? "))
        answer = calculate(number1, char, number2)
        resume = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'e' to exit: ")
        if resume == "n":
            calculator()
        elif resume == "e":
            end = set_end(True)
        else:
            number1 = answer
        end = get_end()

calculator()