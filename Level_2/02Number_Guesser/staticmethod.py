# Level 2 - Task 2: Number Guesser (Static Method (@staticmethod))
import random
class Guesser:
    @staticmethod
    def play():
        l = int(input("Enter lower bound: "))
        h = int(input("Enter upper bound: "))
        target = random.randint(l, h)
        while True:
            g = int(input(f"Guess bt {l} and {h}: "))
            if g < target:
                print("Too low")
            elif g > target:
                print("Too high")
            else:
                print("Correct!")
                break

if __name__ == "__main__":
    Guesser.play()
