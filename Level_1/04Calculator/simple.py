# Level 1 - Task 4: Calculator (Simple Method (function/loop))
def calc():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+ - * / %): ")
    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b != 0:
            print("Result:", f'{a / b:.2f}')
        else:
            print("Cannot divide by 0")
    elif op == "%":
        if b != 0:
            print("Result:", a % b)
        else:
            print("Cannot modulo by 0")
    else:
        print("Invalid operator")
    

if __name__ == "__main__":
    calc()
