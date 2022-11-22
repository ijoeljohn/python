import random

number = random.randrange(1,10)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("please guess a number between 1 and 9  When you want to end the game enter 'exit':")

    if guess == 'exit':
        print("game over")
        break

    guess = int(guess)
    count += 1
    if guess not in range(1,10):
        print("You have to guess a number between 1 and 9!")
    elif guess < number:
        print("gussed to low")
    elif guess > number:
        print("gussed to high")
    else:
        if count == 1:
            print("You rock! You've got it at the first try!")
        elif count <= 3:
            print("Well done! You've got it in just {} tries".format(count))
        elif count > 3:
            print("You've got it! It took you {} tries!".format(count))