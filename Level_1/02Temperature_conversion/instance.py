# Level 1 - Task 2: Temperature Conversion (Instance Method (object level))
class TempConv:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.upper()

    def convert(self):
        if self.unit == "C":
            return (self.value * 9/5) + 32,"F"
        elif self.unit == "F":
            return (self.value - 32) * 5/9,"C"
        else:
            raise ValueError("Invalid unit")

if __name__ == "__main__":
    val = float(input("Enter temperature value: "))
    unit = input("Enter unit (C/F): ")
    obj = TempConv(val, unit)
    res_val, res_unit = obj.convert()
    print(f'{val}{unit.upper()} = {res_val:.2f}{res_unit}')
    
