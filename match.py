#This program competes a user with a compute to match a win
import random
user_won = 0
computer_won = 0

options = ["life","death","god"]

while True:

    user_input = input("Please enter life/death/god or Q to quit ").lower()

    

    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_input = random.randint(0,2)
    computer_input = options[random_input]

    if user_input == "life" and computer_input =="life":
        print("you win")
        user_won += 1
    elif user_input =="god" and computer_input =="death":
        print("you win")
        user_won += 1
    else:
        print("computer win")
        computer_won += 1
        

print("user_won ", user_won, " times")
print("computer_won ", computer_won, " times")
print("Good Bye")
