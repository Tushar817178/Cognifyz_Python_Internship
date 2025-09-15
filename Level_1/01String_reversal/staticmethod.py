# Level 1 - Task 1: String Reversal (Static Method (@staticmethod))
class StringReverser:
    @staticmethod
    def reverse(text):
        return "".join(reversed(text))

if __name__ == "__main__":
    user = input("Enter a string: ")
    print("Reversed String:", StringReverser.reverse(user))
