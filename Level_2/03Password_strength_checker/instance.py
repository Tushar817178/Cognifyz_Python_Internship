# Level 2 - Task 3: Password Strength Checker (Instance Method (object level))
class PassCheck:
    def __init__(self, pas):
        self.pas = pas
    def score(self):
        s = 0
        if len(self.pas) >= 6:
            s+=1
        if any(c.islower() for c in self.pas):
            s+=1
        if any(c.isupper() for c in self.pas):
            s+=1
        if any(c.isdigit() for c in self.pas):
            s+=1
        if any(not c.isalnum() for c in self.pas):
            s+=1
        if s <= 2:
            return "Weak"
        elif s == 3 or s == 4:
            return "Moderate"
        else:
            return "Strong"

if __name__ == "__main__":
    p = input("Enter password: ")
    pc = PassCheck(p)
    print("Strength :", pc.score())
