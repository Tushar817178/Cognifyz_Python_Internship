# Level 2 - Task 1: Guessing Game (Static Method (@staticmethod))
import random
class Game:
    @staticmethod
    def play(st=1, end=100):
        target = random.randint(st, end)
        while True:
            try:
                g = int(input("Guess no between 1 and 100: "))
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
