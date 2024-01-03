# LAB 1.1
# CÂU A
n = int(input("Nhập vào số n:"))
if n < 0: 
    print("Nhập lại số nguyên dương")
else:
    tong = 0
    for i in range(1, n+1):
        tong += i
    print("Giá trị của tổng là:", tong)
# CÂU B
n = int(input("Nhập vào số n:"))
if n < 0: 
    print("Nhập lại số nguyên dương")
else:
    tong = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            tong += i
    print("Giá trị của tổng là:", tong)
#CÂU C
n = int(input("Nhập vào số n:"))
if n < 0: 
    print("Nhập lại số nguyên dương")
else:
    tong = 0
    for i in range(1, n+1):
        if i % 2 !=0:
            tong += i
    print("Giá trị của tổng là:", tong)

# CÂU D
n = int(input("Nhap vao so nguyen duong n: "))
tich = 1
for i in range(1, n+1):
    tich = tich*i
print("D=",tich)
#Câu E
n = int(input("Nhập vào số n:"))
if n < 0: 
    print("Nhập lại số nguyên dương")
else:
    tich = 1
    for i in range(1, n+1):
        if i % 3 ==0:
            tich *= i
    print("E:", tich)
# Câu F
#Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    flag = False 
    if n < 2:
        return flag 
    else:
        for i in range(2, n):
            if n % i == 0:
                return flag
        flag = True
        return flag 
n = int(input("Nhập vào số n:"))

#Chương trình chính
if n < 0: 
    print("Nhập lại số nguyên dương")
else:
    tong = 0
    for i in range(1, n+1):
        if kiem_tra_so_nguyen_to(i):
            tong += i
    print("F:", tong)

# câu G
    n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
flag = True
for i in range(1, n+1):
    if flag == True:
        tong = tong + 1/i
        flag = False
    else:
        tong = tong - 1/i
        flag = True
print("G=",tong)
# câu H
import math 
n = int(input("Nhập vào số n:"))
if n < 0: 
    print("Nhập lại số nguyên dương")
else:
    tong = 0
    for i in range(1, n+1):
        tong += math.sqrt(i) 
    print("Giá trị của tổng là: {:.4f}".format(tong))