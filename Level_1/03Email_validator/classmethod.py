# Level 1 - Task 3: Email Validator (Class Method (@classmethod))
import re
class EmailCheck:
    pattern = r'^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]+\.[a-zA-Z]{2,}$'

    @classmethod
    def is_valid(cls, address):
        return bool(re.fullmatch(cls.pattern , address))
        
if __name__ == "__main__":
    e = input("Enter email: ")
    print("Valid" if EmailCheck.is_valid(e) else "Invalid")
