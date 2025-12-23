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

racers = get_number_of_racers()
print(racers)

