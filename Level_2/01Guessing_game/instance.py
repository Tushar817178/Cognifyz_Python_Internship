# Level 2 - Task 1 : Guessing Game (Instance Method (object level))
import random
class Game:
    def __init__(self, start=1, end=100):
        self.target = random.randint(start, end)
    def guess(self):
        while True:
            try:
                g = int(input("Guess num between 1 and 100: "))
            except ValueError:
                print("Enter integer")
                continue
            if g < self.target:
                print("Too low")
            elif g > self.target:
                print("Too high")
            else:
                print("Correct!")
                break

if __name__ == "__main__":
    g = Game()
    g.guess()
