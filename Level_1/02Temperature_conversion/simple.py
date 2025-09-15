# Level 1 - Task 2: Temperature Conversion (Simple Method (function/loop))
def convert():
    temp = float(input("Enter temperature: "))
    unit = input("Enter Unit (C/F): ")

    if unit.upper() == "C":
        f = (temp * 9/5) + 32
        print(f'{temp}{unit.upper()} = {f:.2f}F')

    elif unit.upper() == "F":
        celsius = (temp - 32) * 5/9
        print(f'{temp}{unit.upper()} = {celsius:.2f}C')

    else:
        print("Please add unit C or F")
    

if __name__ == "__main__":
    convert()
