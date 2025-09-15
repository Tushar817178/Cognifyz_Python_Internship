# Level 1 - Task 3: Email Validator (Instance Method (object level))
import re

class EmailCheck:
    def __init__(self, address):
        self.address = address.strip()

    def is_valid(self):
        pattern = r'^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(pattern,self.address):
           return True
        else:
           return False

if __name__ == "__main__":
    e = input("Enter email: ")
    obj = EmailCheck(e)
    print("Valid" if obj.is_valid() else "Invalid")
