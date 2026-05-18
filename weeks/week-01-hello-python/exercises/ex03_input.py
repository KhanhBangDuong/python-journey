"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào

ten = input("Nhập tên của bạn: ")

print(f"Xin chào, {ten}!")


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!

tuoi = int(input("Nhập tuổi của bạn: "))

nam_hien_tai = 2026
nam_sinh = nam_hien_tai - tuoi

print(f"Bạn sinh năm {nam_sinh}")


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng

so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))

tong = so1 + so2

print(f"Tổng: {so1} + {so2} = {tong}")


# TODO 4 (Thử thách): Tạo Mad Libs mini

ten = input("Nhập một cái tên: ")
tinh_tu = input("Nhập một tính từ: ")
con_vat = input("Nhập tên một con vật: ")
so = input("Nhập một con số: ")

print("\n--- Câu chuyện vui ---")

print(f"Một ngày nọ, {ten} gặp một con {con_vat} rất {tinh_tu}.")
print(f"Cả hai cùng chạy {so} vòng quanh công viên và cười rất vui!")
