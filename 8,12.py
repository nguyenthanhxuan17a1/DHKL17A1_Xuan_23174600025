n = int(input("Nhập một số nguyên: "))
if n < 2:
    print(n,"không phải là số nguyên tố")
else:
    N = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            N = False
            break
    if N:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")