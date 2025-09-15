# Level 1 - Task 5: Palindrome Checker (Simple Method (function/loop))


def palindromeCheck(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]




if __name__ == "__main__":
    text = input("Enter text: ")
    print("Palindrome" if palindromeCheck(text) else "Not a palindrome")
