so_cho = int(input("Nhập số chỗ (4 hoặc 7): "))
quang_duong = float(input("Nhập quãng đường di chuyển (km): "))
thoi_gian_cho = float(input("Nhập thời gian chờ (phút): "))
don_gia_mở_cửa_4_cho = 11000
don_gia_mở_cửa_7_cho = 13000
if quang_duong <20 :don_gia_km_4_cho = 12100 
if quang_duong >20 :don_gia_km_4_cho= 10000
if  quang_duong <30:don_gia_km_7_cho = 14100
if quang_duong >30 : don_gia_km_7_cho=12000
if thoi_gian_cho<=5: don_gia_cho_4_cho  = 0
if thoi_gian_cho >5 :don_gia_cho_4_cho=800
if thoi_gian_cho<=5: don_gia_cho_7_cho  = 0
if thoi_gian_cho >5 :don_gia_cho_7_cho=800
if so_cho == 4:
    cuoc_xe_taxi = don_gia_mở_cửa_4_cho + quang_duong * don_gia_km_4_cho + thoi_gian_cho * don_gia_cho_4_cho
elif so_cho == 7:
    cuoc_xe_taxi = don_gia_mở_cửa_7_cho + quang_duong * don_gia_km_7_cho + thoi_gian_cho * don_gia_cho_7_cho
else:
    cuoc_xe_taxi = 0
print("Cước xe taxi:", cuoc_xe_taxi, "đồng")