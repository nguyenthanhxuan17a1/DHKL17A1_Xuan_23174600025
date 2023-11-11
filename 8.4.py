
a,b,c = eval(input("Nhập độ dài cạnh a,b,c: "))
if a + b > c and b + c > a and c + a > b:
    import math
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Diện tích tam giác là:", S)
else:
    print("Đây không phải là tam giác")