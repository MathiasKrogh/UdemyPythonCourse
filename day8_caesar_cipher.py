from day8_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, cipher_shift, cipher_direction):
    new_text = ""
    if cipher_direction == "decode":
        cipher_shift *= -1
    for char in start_text:
        if char in alphabet:
            index = (alphabet.index(char) + cipher_shift) % 26
            new_text += alphabet[index]
        else:
            new_text += char
    print(f"The {cipher_direction}d text is {new_text}")

print(logo)
end_of_program = False

while not end_of_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    retry = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if retry == "no":
        end_of_program = True
print("Goodbye, have a nice day.")