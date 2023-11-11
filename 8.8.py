so_dem = int(input("Nhập số đêm thuê: "))
menh_gia_phong = int(input("Nhập mệnh giá của phòng (đồng/đêm): "))
if so_dem < 2:
    tien_thue = menh_gia_phong * so_dem
elif so_dem < 4:
    tien_thue = menh_gia_phong * so_dem * 0.75  
else:
    tien_thue = menh_gia_phong * so_dem * 0.7  
print("Số tiền thuê resort:", tien_thue, "đồng")