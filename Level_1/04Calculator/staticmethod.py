# Level 1 - Task 4: Calculator (Static Method (@staticmethod))
class Calculator:
    @staticmethod
    def operate(a, b, op):
        a = float(a); b = float(b)
        if op == "+": return a + b
        if op == "-": return a - b
        if op == "*": return a * b
        if op == "/":
            if b==0:
                return "Div by zero not possible"
            else:
                return a/b
        if op == "%":
            if b==0:
                return "Mod by zero not possible"
            else:
                return a%b

if __name__ == "__main__":
    a = input("Enter first number: "); b = input("Enter second number: ")
    op = input("Enter operator (+ - * / %): ").strip()
    try:
        print("Result:", Calculator.operate(a, b, op))
    except Exception as e:
        print(e)
