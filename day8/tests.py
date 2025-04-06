def greet(name):
    print(f"Hello {name}")
    print(f"I'm also {name}")
    print("How do you do?")

greet(input("What's your name? "))

def greet_name_and_location(name, location):
    print(f"Hello {name} from {location}.")
    print(f"How is it to live in {location}?")

#Functions with keyword arguments
greet_name_and_location(location = input("Where are you from? "), name = input("What's your name? "))

number = (2 - 7) % 26
print(number)
