#Viết một chương trình nhận vào chuỗi "Python is fun"
# câu 1
#Sử dụng len()
string ='Python is fun'
do_dai = len(string)
print("Độ dài chuỗi là:", do_dai)
# câu 2
#In ra chuỗi đảo ngược
chuoi_dao= string[::-1]
print("Chuỗi đảo ngược là:",chuoi_dao)
# câu 3
upper_string =""
for char in string:
    if 'a' <= char <= 'z':
        upper_char = chr(ord(char)-32)
        upper_string += upper_char
    else:
        upper_string += char
print("Chuyển đổi chữ hoa:", upper_string)
# câu 4
#Nhập từ thay thế từ fun
tu_thay_the= input("Nhập vào từ cần thay thế:")
tu_moi = input("Nhập vào từ thay thế:")
chuoi_moi = string.replace(tu_thay_the,tu_moi)
print("Chuỗi sau khi thay thế:",chuoi_moi)
# câu 5
def loai_bo_khoang_trang(chuoi):
    chuoi = chuoi.strip()
    tu = chuoi.split()
    chuoi_moi = ' '.join(tu)
    return chuoi_moi
chuoi = " Hello,   Python! "
chuoi_hop_le = loai_bo_khoang_trang(chuoi)
print(chuoi_hop_le)
# câu 6
def tach_chuoi(chuoi):
    danh_sach_tu = chuoi.split()
    return danh_sach_tu
chuoi = input("Nhập chuỗi: ")
danh_sach_tu = tach_chuoi(chuoi)
print("Danh sách các từ là:", danh_sach_tu)

