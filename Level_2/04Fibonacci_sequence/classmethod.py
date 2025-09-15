# Level 2 - Task 4: Fibonacci Sequence (Class Method (@classmethod))
class Fib:
    @classmethod
    def generate(cls, n):
        a,b = 0,1
        res = []
        for i in range(n):
            res.append(a)
            a,b = b, a+b
        return res

if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    print(Fib.generate(n))
