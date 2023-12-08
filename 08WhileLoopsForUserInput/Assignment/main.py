import random

def number_guesser():
    random_number = random.randint(1, 10)
    guess = ""
    incorrect_guess = True
    while incorrect_guess == True:
        print("guess a number")
        guess = int(input())

        if guess > random_number:
            print("too high")
        elif guess < random_number:
            print("too low")
        elif guess == random_number:
            incorrect_guess = False
    
    print("correct")

number_guesser()
    

def number_guesser_with_lives():
    lives = 3
    random_number = random.randint(1, 10)
    guess = ""
    incorrect_guess = True
    while incorrect_guess == True:
        print("guess a number")
        guess = int(input())

        if guess > random_number:
            print("too high")
            lives = lives - 1
        elif guess < random_number:
            print("too low")
            lives = lives - 1
        elif lives == 0:
            print("out of lives")
            incorrect_guess = False
        elif guess == random_number:
            incorrect_guess = False
    
    print("correct")

number_guesser_with_lives()