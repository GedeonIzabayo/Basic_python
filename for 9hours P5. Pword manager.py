mater_psw = input("what is a master password? ")

def view():
    pass
def add():
    name = input("Account name: ")
    psw = input("password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + "pwd")

while True:
    mode = input("would like to add a new password or view existing one (view, add), press q to quit? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue

