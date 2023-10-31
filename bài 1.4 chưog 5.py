import math
a= int(input("Nhập độ dài cạnh a :"))
b= int(input("Nhập độ dài cạnh b :"))
c= int(input("Nhập độ d ài cạnh c :"))
p= (a+b+c)/2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Diện tích tam giác :",S)
a=7
b=5
c=2