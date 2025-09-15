# Level 1 - Task 3: Email Validator (Simple Method (function/loop))
import re
def check_email(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern,email):
        return True
    else:
        return False
    

if __name__ == "__main__":
    email = input("Enter email: ").strip()
    print("Valid" if check_email(email) else "Invalid")
