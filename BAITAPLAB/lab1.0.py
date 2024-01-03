# bài 1 .0 lab
#1 Kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(so_can_kiem_tra):
    if so_can_kiem_tra <= 1:
        return False
    else:
        for i in range(2, so_can_kiem_tra):
            if so_can_kiem_tra % i == 0:
                return False
        else:
            return True

n = int(input("Nhap vao mot so nguyen duong n: "))
if n < 0:
    print("n phai la so nguyen duong")
else:
    if kiem_tra_so_nguyen_to(n):
        print(n,"la so nguyen to")
    else:
        print(n,"khong phai so nguyen to")
        
# 2. Kiểm tra số chính phương
        n = int(input("Nhập số n="))
flag= False
 
for i in range(1, n + 1 ):
    if (i**2 == n):
        flag = True
        break
 
if (flag == True):
    print(n, " là số chính phương")
else:
    print(n, " không phải là số chính phương")
    
    #3.Kiểm tra là số hoàn hảo
    n = int(input("Nhập số n:"))
tong = 0
 
for i in range(1, n):
    if (n % i == 0):
        tong += i
 
if (tong == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")
#4.Kiểm tra là số lẻ
n=int(input("Nhập số N:"))
if n %2 !=0:
    print(n,"là số lẻ")
else:
    print(n,"không là số lẻ")
#5.Kiểm tra là số chẵn
    n=int(input("Nhập số N:"))
if n %2 ==0:
    print(n,"là số chẵn ")
else:
    print(n,"là số lẻ")
#6.Kiểm tra só fibonacci
def kiem_tra_so_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

n= int(input("Nhập số cần kiểm tra: "))
if kiem_tra_so_fibonacci(n):
    print(n, "là số Fibonacci.")
else:
    print(n, "không phải là số Fibonacci.")
    #7 Kiểm tra số đói xứng
def kiem_tra_doi_xung(so):
    chs = str(so)
    if len(chs) <= 1:
        return False
    else:
        if chs == chs[::-1]:
            return True
        else:
            return False

n = int(input("Nhap vao mot so nguyen duong n: "))
if n < 0:
    print("n phai la so nguyen duong")
else:
    if kiem_tra_doi_xung(n):
        print(n,"la so doi xung")
    else:
        print(n,"khong phai so doi xung")
#8 kiểm tra số Harshad
def kiem_tra_so_harshad(n):
    flag = False
    sum = 0 
    a = str(n)
    for i in a:
        sum += int(i)
    if n % sum == 0:
        flag = True
    return flag
n = int(input('Nhập vào số n:'))

if kiem_tra_so_harshad(n):
    print(n, 'là số harshad')
else:
    print(n, 'không là số harshad')
    
#9 Tìm uCLn
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if a > 0 and b > 0:
    min = a
    if min >= b:
        min = b
    while True:
        if a % min == 0 and b % min == 0:
            break
        else:
            min -= 1
    print("UCNN của hai số ", a, " và ", b," là: ", min)
else:
    print("Yêu cầu nhập 2 số nguyên dương")
# 10, tìm bcnn
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if a > 0 and b > 0:
    max = a
    if max <= b:
        max = b
    while True:
        if max % a == 0 and max % b == 0:
            break
        else:
            max += 1
    print("BCNN của hai số ", a, " và ", b," là: ", max)
else:
    print("Yêu cầu nhập 2 số nguyên dương")


# Vận dụng
    






 