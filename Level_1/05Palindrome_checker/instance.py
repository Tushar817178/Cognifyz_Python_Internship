# Level 1 - Task 5: Palindrome Checker (Instance Method (object level))
class Pal:
    def __init__(self, text):
        self.text = text
    def check(self):
         word = self.text.lower().replace(" ", "")
         return word == word[::-1]

if __name__ == "__main__":
    t = input("Enter text: ")
    obj = Pal(t)
    print("Palindrome" if obj.check() else "Not a palindrome")
