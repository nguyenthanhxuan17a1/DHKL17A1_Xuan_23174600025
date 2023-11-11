N = int(input("Nhập số lượng số nguyên cần tính tổng: "))
S= 0
for i in range(N):
    x = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
    S+= x
print("Tổng của các số nguyên là:",S)