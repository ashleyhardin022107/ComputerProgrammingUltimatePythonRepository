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

# number_guesser()
    

def number_guesser_with_lives():
    lives = 3
    print("lives: ", lives)
    random_number = random.randint(1, 10)
    guess = ""
    incorrect_guess = True
    while incorrect_guess == True and lives >= 1:
        print("guess a number")
        guess = int(input())

        if guess > random_number:
            print("too high")
            lives = lives - 1
            print("lives: ", lives)
        elif guess < random_number:
            print("too low")
            lives = lives - 1
            print("lives: ", lives)
        elif lives == 0:
            print("out of lives")
            incorrect_guess = False
        elif guess == random_number:
            incorrect_guess = False
    
    print("correct")

#number_guesser_with_lives()


def vending_machine():
    quarter = 25
    dime = 5
    nickle = 10
    amount_due = 50
    coin_input = ""
    invalid_coin = True
    while invalid_coin == True:
        print("amount due: ", amount_due)
        coin_input = int(input())

        if coin_input == quarter or coin_input == dime or coin_input == nickle:
            amount_due = amount_due - coin_input
            


    