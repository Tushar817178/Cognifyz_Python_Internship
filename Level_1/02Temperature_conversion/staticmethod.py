# Level 1 - Task 2: Temperature Conversion (Static Method (@staticmethod))
class TempConv:
    @staticmethod
    def c2f(c): return (c * 9/5) + 32
    @staticmethod
    def f2c(f): return (f - 32) * 5/9

if __name__ == "__main__":
    val = float(input("Enter temperature value: "))
    unit = input("Enter unit (C/F): ").upper()
    if unit == "C":
        print(f"{val}C = {TempConv.c2f(val):.2f}F")
    elif unit == "F":
        print(f"{val}F = {TempConv.f2c(val):.2f}C")
    else:
        print("Invalid unit.")
