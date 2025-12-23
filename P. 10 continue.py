import turtle
import time

WIDTH, HEIGHT = 500, 500

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('turtle racing!')

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('enter number of racers (2 -10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric...try agin!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('number not in range 2-10. try again!')

def init_turtle():
    screen.bgcolor("lightblue")
    screen.setup(WIDTH, HEIGHT)
    screen.title('turtle racing!')

racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.shape("turtle")
racer.color("green")
racer.forward(100)
time.sleep(5)
