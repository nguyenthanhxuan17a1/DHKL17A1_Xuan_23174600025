
lai_suat_nam = float(input("Lãi suất 1 năm (%): "))
so_tien_gui = float(input("Số tiền gửi (VND): "))
so_thang = input("Số tháng gửi: ")
lai_suat_thang = lai_suat_nam / 100 / 12
tien_lai = so_tien_gui * so_thang * lai_suat_thang
tong_so_tien = so_tien_gui + tien_lai
print("Tiền lãi:",tien_lai)
print(f"Tổng số tiền sau khi hết thời hạn gửi tiền:",tong_so_tien)
