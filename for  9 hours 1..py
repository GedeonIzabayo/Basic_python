print("welcome to my computer quiz!")

playing = input("do you want to play? ")
print (playing)

if playing != "yes":
    quit()

print("Okey! let's play")

answer = input("what does CPU stands for? ")
if answer == "central processing unit":
    print('correct!' )
    score = 0
else:
    print("incorrect!")


answer = input("what does GPU stands for? ")
if answer == "graphics processing unit":
    print('correct!' )
    score += 1
else:
    print("incorrect!")


answer = input("what does RAM stands for? ")
if answer == "random access memory":
    print('correct!' )
    score += 1
else:
    print("incorrect!")

answer = input("what does PSU stands for? ")
if answer == "power supply":
    print('correct!' )
    score += 1
else:
    print("incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 4) * 100) + "%.")
text = "TIM IS GREAT!"
print(text.lower())








