import random

top_number = input("Please enter a top number ")

if top_number.isdigit():
    top_number = int(top_number)
    random_num = random.randint(0,top_number)
    print("generated random number is: " , random_num)
else:
    print("please enter only a number")
    quit()
    #print("you entered: " + str(top_number))


while True:

    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_num:
            print("you guess correct")
            break
        else:
            print("you guessed incorrect")
            continue
    else:
        print("Please enter only number")
        break
