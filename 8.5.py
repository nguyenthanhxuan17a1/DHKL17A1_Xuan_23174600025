nam= int(input("Nhập năm:"))
if nam % 4 == 0:
    if nam % 100 == 0:
        if nam % 400 == 0:
            print(nam,"là năm nhuận")
        else:
            print(nam,"không phải là năm nhuận")
    else:
        print(nam,"là năm nhuận")
else:
    print(nam,"không phải là năm nhuận")