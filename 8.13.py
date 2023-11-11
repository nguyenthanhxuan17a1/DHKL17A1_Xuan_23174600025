n = int(input("Nhập một số nguyên n: "))
sum_odd = 0
for i in range(1, n+1, 2):
    sum_odd += i
A= sum_odd
print("Giá trị của biểu thức A:",A)
sum_even = 0
for i in range(0, n+1, 2):
    sum_even += i
B = sum_even
print("Giá trị của biểu thức B:", B)
tich = 1
for i in range(1, n+1):
    tich *= i
C = tich
print("Giá trị của biểu thức C:", C)
tich = 1
for i in range(1, n+1):
    if i % 3 == 0:
        tich *= i
D = tich
print("Giá trị của biểu thức D:", D)
sum_prime = 0
for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        sum_prime += i
E = sum_prime
print("Giá trị của biểu thức E:", E)
sum_dan_dau = 0
for i in range(1, n+1):
    if i % 2 == 1:
        sum_dan_dau += i
    else:
        sum_dan_dau -= i
F = sum_dan_dau
print("Giá trị của biểu thức F:", )