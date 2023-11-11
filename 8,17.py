a=int(input("Nhap so nguyen a:"))
b=int(input("Nhap so nguyen b:"))
while(a*b != 0):
    if a>b:
        a %= b
    else:
        b %= a
print(a+b)