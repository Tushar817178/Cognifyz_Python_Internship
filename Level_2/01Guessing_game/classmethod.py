# Level 2 - Task 1: Guessing Game (Class Method (@classmethod))
import random
class Game:
    @classmethod
    def play(cls, start=1, end=100):
        target = random.randint(start, end)
        while True:
            try:
                g = int(input("Guess a num between 1 and 100: "))
            except ValueError:
                print("Enter integer")
                continue
            if g < target:
                print("Too low")
            elif g > target:
                print("Too high")
            else:
                print("Correct!")
                break

if __name__ == "__main__":
    Game.play()
