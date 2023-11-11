S = 0
while True:
    x = int(input("Nhập một số nguyên (nhập 0 để dừng): "))
    if x == 0:
        break
    S+= x
print("Tổng của các số nguyên là:",S)