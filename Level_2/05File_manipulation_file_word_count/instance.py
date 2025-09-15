# Level 2 - Task 5: File Word Count (Instance Method (object level))
from collections import Counter
class FileCounter:
    def __init__(self, path):
        self.path = path
    def count(self):
        try:
             with open(self.path , "r" , encoding = "utf-8")as f:
                 text = f.read()
        except FileNotFoundError:
            print("File not found")
            return

        words = text.split()
        n = len(words)

        for i in range(n):
            word = words[i].lower()
            if word == "":
                 continue

            count = 1
            for j in range(i+1,n):
                if word == words[j].lower():
                    count +=1
                    words[j] = ""
            print(word,":",count)
       

if __name__ == "__main__":
    p = input("Enter file path: ")
    fc = FileCounter(p)
    fc.count()
