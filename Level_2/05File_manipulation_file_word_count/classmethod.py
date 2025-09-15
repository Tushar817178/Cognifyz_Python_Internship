# Level 2 - Task 5: File Word Count (Class Method (@classmethod))
from collections import Counter
class FileCounter:
    @classmethod
    def count(cls, path):
         try:
             with open(path , "r" , encoding = "utf-8")as f:
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
    FileCounter.count(p)
