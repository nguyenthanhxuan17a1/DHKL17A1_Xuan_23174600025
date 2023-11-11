n=eval(input("Nhap vao mot day so:"))
h_num = list(range(n, 0 , -1))
print("", h_num)
print("Day so le dao nguoc la:")
for num in h_num:
    if num % 2 !=0:
        print("", num)