"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân

ten = "Dương Khánh Băng"   # str
tuoi = 20                  # int
diem_tb = 8.5              # float
dang_hoc = True            # bool

# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()

print(ten, type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc, type(dang_hoc))


# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm

a = 10
b = 20

print("Trước hoán đổi:")
print("a =", a)
print("b =", b)

# Hoán đổi
a, b = b, a

print("Sau hoán đổi:")
print("a =", a)
print("b =", b)


# TODO 3: Augmented assignment

x = 100

x += 50
print("Sau += :", x)

x -= 20
print("Sau -= :", x)

x *= 2
print("Sau *= :", x)

x //= 5
print("Sau //= :", x)


# TODO 4 (Thử thách): Multiple assignment

ho, ten, tuoi = "Dương", "Khánh Băng", 20

print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")
