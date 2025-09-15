# Level 1 - Task 1: String Reversal (Instance Method (object level))
class StringReverser:
    def __init__(self, text):
        self.text = text
    def reverse(self):
        return self.text[::-1]

if __name__ == "__main__":
    user = input("Enter a string: ")
    obj = StringReverser(user)
    print("Reversed string:", obj.reverse())
