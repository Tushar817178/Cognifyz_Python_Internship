# Level 2 - Task 3: Password Strength Checker (Simple Method (function/loop))
def strength(pwd):
    score = 0
    if len(pwd) >= 6:
        score += 1
    if any(c.islower() for c in pwd):
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(not c.isalnum() for c in pwd):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"
    

if __name__ == "__main__":
    p = input("Enter password: ")
    s = strength(p)
    print("Strength :", s)



