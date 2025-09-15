# Level 1 - Task 1: String Reversal (Class Method (@classmethod))
class StringReverser:
    @classmethod
    def reverse(cls, text):
        return text[::-1]

if __name__ == "__main__":
    user = input("Enter a string: ")
    print("Reversed String:", StringReverser.reverse(user))
