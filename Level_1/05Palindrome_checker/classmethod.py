# Level 1 - Task 5: Palindrome Checker (Class Method (@classmethod))
class Pal:
    @classmethod
    def check(cls, text):
        text = text.lower().replace(" ","")
        return text==text[::-1]

if __name__ == "__main__":
    t = input("Enter text: ")
    print("Palindrome" if Pal.check(t) else "Not a palindrome")
