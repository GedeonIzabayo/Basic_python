2D lists = a list of lists

drinks = ["coffee","soda", "tea"]
dinner = ["pizza","hamburger", "hotdog"]
dessert  =["cake", "ice cream"]

food  = [drinks, dinner, dessert]

print(food)
print(food[0])
print(food[0][1])

def hello(first, middle, last):
    print("hello "+ first+ " "+middle+" "+last)

hello("Gedeon", "Waggner", "code")

name = "Gedeon"

print("hello, my name is {}".format(name))
print("hello, my name is {:10}. nice to meet you".format(name))

