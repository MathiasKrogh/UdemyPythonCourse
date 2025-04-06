import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rsc = [rock, scissors, paper]
human = int(input("Hvad vælger du? 0 for sten, 1 for saks og 2 for papir.\n"))
if human < 0 or 2 < human:
    print("You typed an invalid number and lose by default...")
    exit()
print(f"{rsc[human]}\n")

computer = random.randint(0, 2)
print(f"Computeren valgte: {rsc[computer]}")



if human == computer:
    print("Uafgjort...")
elif (human == 0 and computer == 2) or (human == 1 and computer == 0) or (
        human == 2 and computer == 1):
    print("Du tabte...")
else:
    print("Du vandt!")
exit()