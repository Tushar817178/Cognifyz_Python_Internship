# Level 2 - Task 2: Number Guesser (Simple Method (function/loop))
import random
try:
    start = int(input("Enter lower bound: "))
    end = int(input("Enter upper bound: "))
except ValueError:
    print("Enter integers")
    raise SystemExit
if start >= end:
    print("Lower should be less than upper")
    raise SystemExit
    
target = random.randint(start, end)
while True:
    try:
        g = int(input(f"Guess between {start} and {end}: "))
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
