name = input("type your name: ")
print("welcome", name, " to this adventure!")

answer = input(
    "you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? " ).lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim across?  type to walk around and swim across: ")

    if answer == "swim":
        print("you swim across and were eaten by alligator")

    elif answer == "walk":
       print("you walked for many miles and run out of water and you lost the game.")

    else:
        print("not a valid option. you lose!")

elif answer == "right":
   answer = input("you come to bridge, it looks wobbly, do you want to cross it or head back(cross/back) ? ")

   if answer == "back":
       answer = input("you back and loose!")

       print("you back and lose!.")

   elif answer == "cross":
       answer = input("you cross the bridge and meet a stranger. do you talk them(yes/no)?")

       if answer == "yes":
           print("you talk to the stranger and they give you gold. you win!")

       elif answer == "no":
           print("you ignore the stranger and they are offended and you lose.")

       else:
           print("not a valid option. you lose!")

print("thank you for trying", name)