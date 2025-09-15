# Level 1 - Task 5: Palindrome Checker (Static Method (@staticmethod))
class Pal:
    @staticmethod
    def check(text):
        word = text.lower().replace(" ","")
        return word == word[::-1]

if __name__ == "__main__":
    t = input("Enter text: ")
    print("Palindrome" if Pal.check(t) else "Not a palindrome")
