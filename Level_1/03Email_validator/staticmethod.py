# Level 1 - Task 3: Email Validator (Static Method (@staticmethod))
import re
class EmailCheck:
   

    @staticmethod
    def check(mail):
         pattern = r'^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]+\.[a-zA-Z]{2,}$'
         return re.fullmatch(pattern , mail) is not None
        
if __name__ == "__main__":
    e = input("Enter email: ")
    print("Valid" if EmailCheck.check(e) else "Invalid")

