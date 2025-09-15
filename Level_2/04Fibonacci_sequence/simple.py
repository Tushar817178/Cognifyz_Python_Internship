# Level 2 - Task 4: Fibonacci Sequence (Simple Method (function/loop))
def fib(n):
    a,b = 0,1
    res = []
    for i in range(n):
        res.append(a)
        a,b = b, a+b
    return res

if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    print(fib(n))
