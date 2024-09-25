#writing and reading a password file
from cryptography.fernet import Fernet
master_password = input("please enter the master password ").lower()

def add():

    acct = input("account name: ")
    passwd = input("password: ")

    try:
        with open("password3.txt", "a") as f:
            f.write(acct + "|" +passwd +"\n")
    except FileNotFoundError:
        print("File not found exception")
        
def view():
    try:
        with open("password8.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("user:" ,user ," password: " ,passw)
    except FileNotFoundError:
         print("File not found")
            

while True:
    user_action = input("What would you like to do ? add or view or q to quit ").lower()

    if user_action == "add":
        add()

    elif user_action == "view":
        view()
    elif user_action == "q":
        break

    else:
        print("please enter add or view or quit")
        continue
