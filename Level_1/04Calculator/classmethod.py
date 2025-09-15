# Level 1 - Task 4: Calculator (Class Method (@classmethod))
class Calculator:
    @classmethod
    def operate(cls, a, b, op):
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
    a = input("Enter first number: ");
    b = input("Enter second number: ")
    op = input("Enter operator (+ - * / %): ").strip()
    print("Result:", Calculator.operate(a, b, op))
    
