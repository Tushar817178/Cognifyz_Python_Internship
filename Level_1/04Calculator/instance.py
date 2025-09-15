# Level 1 - Task 4: Calculator (Instance Method (object level))
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        if self.b==0:
            return "Div by Zero not possible"
        else:
            return self.a / self.b
    def mod(self):
        if self.b==0:
            return "Mod by Zero not possible"
        else:
            return self.a % self.b





if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    op = input("Enter operator (+ - * / %): ").strip()
    calc = Calculator(a, b)
    if op=="+":
        print("Result:", calc.add())
    if op=="-":
        print("Result:", calc.sub())
    if op=="*":
        print("Result:", calc.mul())
    if op=="/":
        print("Result:", calc.div())
    if op=="%":
        print("Result:", calc.mod())
