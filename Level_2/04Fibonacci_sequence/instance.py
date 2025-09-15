# Level 2 - Task 4: Fibonacci Sequence (Instance Method (object level))
class Fib:
    def __init__(self, n):
        self.n = n
    def generate(self):
        a,b = 0,1
        res = []
        for i in range(self.n):
            res.append(a)
            a,b = b, a+b
        return res

if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    f = Fib(n)
    print(f.generate())
