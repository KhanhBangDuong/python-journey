"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000

ket_qua = 2024 + 1000

print("2024 + 1000 =", ket_qua)


# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.

tien_hien_co = 150000
gia_ca_phe = 35000
so_ly = 3

tien_con_lai = tien_hien_co - (gia_ca_phe * so_ly)

print("Số tiền còn lại =", tien_con_lai, "VNĐ")


# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2

ban_kinh = 7

dien_tich = 3.14159 * ban_kinh ** 2

print("Diện tích hình tròn =", dien_tich)


# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?

keo = 100
nguoi = 7

moi_nguoi = keo // nguoi
con_du = keo % nguoi

print("Mỗi người được", moi_nguoi, "viên")
print("Còn dư", con_du, "viên")


# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit

c = 37

f = c * 9 / 5 + 32

print(f"{c}°C = {f}°F")
