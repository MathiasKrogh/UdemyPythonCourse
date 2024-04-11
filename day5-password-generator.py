#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("Easy solution:")
easy_password = ""
for letter in range(0, nr_letters):
    easy_password += random.choice(letters)
for number in range(0, nr_numbers):
    easy_password += random.choice(numbers)
for symbol in range(0, nr_symbols):
    easy_password += random.choice(symbols)
print(f"Your password is {easy_password}\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("Hard solution:")
password = ""
sum_of_char = nr_letters + nr_numbers + nr_symbols
list_of_char = []
for letter in range(0, nr_letters):
    list_of_char.append("letter")
for number in range(0, nr_numbers):
    list_of_char.append("number")
for symbol in range(0, nr_symbols):
    list_of_char.append("symbols")

for char in range(0, sum_of_char):
    type_of_char = random.choice(list_of_char)
    if type_of_char == "letter":
        password += random.choice(letters)
    if type_of_char == "number":
        password += random.choice(numbers)
    if type_of_char == "letter":
        password += random.choice(symbols)
    list_of_char.remove(type_of_char)
print(f"Your password is {password}")