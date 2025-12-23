#tuple = collection which is ordered and unchangable
#        used to group together related data

student =("Gedeon", 32,"male")

print(student.count("Gedeon"))
print(student.index("male"))

for x in student:
    print(x)

if "Gedeon" in student:
    print("Gedeon is here!")


