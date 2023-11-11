a=float(input("Nhap so kwh tieu thu:"))
if a>=0:
    if a<=50:
       print("Tien phai tra:",a*1678)
    elif a<=100:
       print("Tien phai tra:",50*1678+(a-50)*1734)
    elif a<=200:
       print("tien phai tra:",50*(1678+1734)+(a-100)*2014)
    elif a<=300:
       print("Tien phai tra:",50*(1678+1734+2014)+(a-200)*2536)
    elif a<=400:
       print("ien phai tra:",50*(1678+1734+2014+2536)+(a-300)*2834)
    else:
       print("Tien phai tra:",50*(1678+1734+2014+2536+2834)+(a-400)*2927)  