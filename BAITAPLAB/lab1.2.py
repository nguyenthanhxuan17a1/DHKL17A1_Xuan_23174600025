# lab1.2
# câu 1
def tim_so_nho_nhat(A):
    n = 1
    sum = 0
    while sum <= A:
        tong += n
        n +=1 
    return (n-1)
A = int(input('Nhập vào số A:'))
min_n = tim_so_nho_nhat(A)
print("Số n nhỏ nhất thỏa mãn là:", min_n)

# câu 2
#Tìm số nguyên nhỏ nhất
def tim_so_nho_nhat(A):
    n = 1
    tong = 0
    while tong <= A:
        tong += n**2
        n +=1 
    return (n-1)
A = int(input('Nhập vào số A:'))
min_n = tim_so_nho_nhat(A)
print("Số n nhỏ nhất thỏa mãn là:", min_n)

# câu 3
#Tìm số nguyên lớn nhất
def tim_so_lon_nhat(A):
    m = 1
    tong = 0
    while tong < A:
        tong += m
        if tong >= A:
            break
        m += 1
    return m - 1

#Chương trình chính
A = int(input('Nhập vào số A:'))
max_m = tim_so_lon_nhat(A)
print("Số m lớn nhất thỏa mãn là:", max_m)
 # câu 4
def tim_so__nho_nhat(A):
    n = 1
    tich = 1
    while tich <= A:
        tich *= n
        n +=1 
    return (n-1)
A = int(input('Nhập vào số A:'))
min_n = tim_so_nho_nhat(A)
print("Số n nhỏ nhất thỏa mãn là:", min_n)