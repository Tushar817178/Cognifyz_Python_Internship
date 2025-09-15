# Level 2 - Task 3: Password Strength Checker (Class Method (@classmethod))
class PassCheck:
    @classmethod
    def score(cls, pwd):
        s = 0
        if len(pwd) >= 8: s+=1
        if any(c.islower() for c in pwd):
            s+=1
        if any(c.isupper() for c in pwd):
            s+=1
        if any(c.isdigit() for c in pwd):
            s+=1
        if any(not c.isalnum() for c in pwd):
            s+=1
        if s <= 2:
            return "Weak"
        elif s== 3 or s== 4:
            return "Moderate"
        else:
            return "Strong"
    

if __name__ == "__main__":
    p = input("Enter password: ")
    print("Strength :", PassCheck.score(p))
