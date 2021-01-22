from random import randint
import statistics


def head_menu():
    choose_choices = input("1. Divisible Function \n"
                           "2. Guessing Game \n"
                           "3. Exit!\n")
    if choose_choices == "1":
        print()
        divisible_list()
    elif choose_choices == "2":
        print()
        guess_number()
    elif choose_choices == "3":
        print("Thank you for your time and welcome back!\n ")
        quit()
    else:
        print("Invalid input, please choose your option between 1-3: ")
        head_menu()


def divisible_list():
    number = [] ##array of numbers
    num1 = 0
    num2 = 0

    while True:
        try:
            num1 = int(input("Enter your first number: "))
            break
        except ValueError:
            print("Invalid input, please try again. ") # if the user entered wrong input

    while True:
        try:
            num2 = int(input("Enter your second number: "))
            break
        except ValueError:
            print("Invalid input, please try again. ")

    for num in range(1, 1001):
        if num % num1 == 0 and num % num2 == 0:
            number.append(num)
    print(number)

    number_median = statistics.mean(number) #import from statistics for median number
    print(f"The value of median is {number_median}. \n")


def guess_number():
    hidden_num = randint(1, 101) #import random numbers between 1 and 100
    count = 0
    guess = 0
    max_guess = 10

    while guess != hidden_num and count != max_guess: # =! is not equal
        while True:
            try:
                guess = int(input("I'm thinking of a number between 1 - 100:\n "))
            except ValueError:
                print("Invalid input, please try again. ")
            if guess > hidden_num:
                count += 1
                print(f"Your guess {count}/{max_guess} is to high, please try again: ")
            elif guess < hidden_num:
                count += 1
                print(f"Your guess {count}/{max_guess} is to low, please try again: ")
            elif guess == hidden_num:
                count += 1
                print(f"That's correct! Number {guess} is correct). Your attempt was {count} times. ")
                print("Thank you for playing! \n")
            break
