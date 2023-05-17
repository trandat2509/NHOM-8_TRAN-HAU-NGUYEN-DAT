def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

x = int(input("Nhập số nguyên dương a: "))
y = int(input("Nhập số nguyên dương b: "))
print("Ước số chung lớn nhất của", x, "và", y, "là:", uscln(x, y))

