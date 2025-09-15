# Level 2 - Task 2: Number Guesser (Class Method (@classmethod))
import random
class Guesser:
    @classmethod
    def play(cls):
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        target = random.randint(low, high)
        while True:
            g = int(input(f"Guess bt{low}and{high}: "))
            if g < target:
                print("Too low")
            elif g > target:
                print("Too high")
            else:
                print("Correct!")
                break

if __name__ == "__main__":
    Guesser.play()
