# Level 1 - Task 1: String Reversal (Simple Method (function/loop))

def reverse_string(string):
    result = ""
    for ch in string:
        result = ch + result
    return result

if __name__ == "__main__":
    user = input("Enter a string: ")
    print("Reversed string:", reverse_string(user))
