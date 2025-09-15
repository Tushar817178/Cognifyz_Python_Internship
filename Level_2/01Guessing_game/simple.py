# Level 2 - Task 1: Guessing Game (Simple Method (function/loop))
import random
def play():
    
    num = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Enter an integer.")
            continue
        if guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
        else:
            print("Correct!")
            break

if __name__ == "__main__":
    play()
