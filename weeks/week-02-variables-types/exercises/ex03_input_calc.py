"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

print("Tổng =", a + b)
print("Hiệu =", a - b)
print("Tích =", a * b)
print("Thương =", a / b)


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r

pi = 3.14159

r = float(input("Nhập bán kính hình tròn: "))

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r

print(f"Diện tích = {dien_tich:.2f}")
print(f"Chu vi = {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm

gia_goc = float(input("Nhập giá gốc: "))
giam_gia = float(input("Nhập phần trăm giảm giá: "))

gia_sau_giam = gia_goc - (gia_goc * giam_gia / 100)

print(f"Giá sau giảm = {gia_sau_giam:,.0f} VNĐ")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ

vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))

usd = vnd / ty_gia

print(f"Số USD tương ứng: {usd:.2f} USD")
