# Level 1 - Task 2: Temperature Conversion (Class Method (@classmethod))
class TempConv:
    @classmethod
    def convert(cls, value, unit):
        unit = unit.upper()
        if unit == "C":
            return f"{value}C ={(value * 9/5) + 32:.2f}F"
        elif unit == "F":
            return f"{value}F = {(value - 32) * 5/9:.2f}C"
        else:
            raise ValueError("Invalid unit")

if __name__ == "__main__":
    val = float(input("Enter temperature value: "))
    unit = input("Enter unit (C/F): ")
    res = TempConv.convert(val, unit)
    print(res)
   
