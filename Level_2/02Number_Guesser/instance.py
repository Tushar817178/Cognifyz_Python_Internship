# Level 2 - Task 2: Number Guesser (Instance Method (object level))
import random
class Guesser:
    def __init__(self, st, end):
        self.st = st
        self.end = end
        self.target = random.randint(st, end)
    def play(self):
        while True:
            g = int(input(f"Guess a num bet {self.st} and{self.end}: "))
            if g < self.target:
                print("Too low")
            elif g > self.target:
                print("Too high")
            else:
                print("Correct!")
                break

if __name__ == "__main__":
    low = int(input("Enter lower bound: "))
    high = int(input("Enter upper bound: "))
    game = Guesser(low, high)
    game.play()
