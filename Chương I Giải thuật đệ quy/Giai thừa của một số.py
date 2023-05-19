def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n-1)

n = int(input("Nhập số nguyên n cần tính giai thừa: "))
ket_qua = giai_thua(n)
print("Giai thừa của",n ,"là:", ket_qua)

    