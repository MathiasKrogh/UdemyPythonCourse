print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_choice = input("You are at a crossroad. Do you go left or right? ").lower()
if first_choice == "left":
  print("You tripped on a rock and break your neck. Game over!")
elif first_choice == "right":
  second_choice = input("You get to a lake. Do you swim across or search for a boat? Write S or B: ").lower()
  if second_choice == "b":
    print("You couldn't find a boat and you end up tripping on a rock and break your neck. Game over!")
  elif second_choice == "s":
    third_choice = input("You swim across the lake and get to a house on the other side. Inside are three doors coloured red, blue and yellow. Which do you go through. Type R, B or Y: ").lower()
    if third_choice == "r":
      print("You go inside the red door. Inside the room is a small rock, so you decide to trip on it and break you neck. Game Over!")
    elif third_choice == "b":
      print("You go inside the blue door and you are met by a chihuahua. It mauls you ankles and you trip and break your neck. Game over!")
    elif third_choice == "y":
      print("You go inside the yellow door and inside is a chest of gold. You win!")
    else:
      print("That wasn't a possibility, fuck you! Game over, clown!")
  else:
    print("That wasn't a possibility, fuck you! Game over, clown!")
else:
  print("That wasn't a possibility, fuck you! Game over, clown!")
  