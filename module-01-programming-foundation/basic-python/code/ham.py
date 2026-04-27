# Cấu trúc của 1 hàm
def ham_chao_mung(ten):
    """Hàm này chào mừng người dùng với tên được cung cấp."""
    # """ là phần chú thích (docstring) của hàm, giúp giải thích chức năng của hàm.
    print(f"Chào mừng, {ten}!")
    # f literals (f-string) được sử dụng để chèn giá trị của biến ten vào trong chuỗi.
    # chữ f trước chuỗi cho phép bạn sử dụng cú pháp {ten} để chèn giá trị của biến ten vào trong chuỗi.

# Gọi hàm
ham_chao_mung("Alice")
# Hàm có thể trả về giá trị
def tinh_tong(a, b):
    """Hàm này trả về tổng của hai số."""
    return a + b

# Gọi hàm và lưu giá trị trả về
ket_qua = tinh_tong(5, 3)
print("Tổng của 5 và 3 là:", ket_qua)

# Hàm có thể có nhiều tham số
def tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    """Hàm này trả về diện tích của hình chữ nhật."""
    return chieu_dai * chieu_rong

# Gọi hàm và lưu giá trị trả về
dien_tich = tinh_dien_tich_hinh_chu_nhat(5, 3)
print("Diện tích của hình chữ nhật là:", dien_tich)

# Hàm có thể có tham số mặc định
def tinh_dien_tich_hinh_tron(ban_kinh, pi=3.14):
    """Hàm này trả về diện tích của hình tròn."""
    return pi * ban_kinh ** 2

# Gọi hàm và lưu giá trị trả về
dien_tich = tinh_dien_tich_hinh_tron(5)
print("Diện tích của hình tròn là:", dien_tich)
# Hàm có thể có tham số tùy chọn
def tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong=None):
    """Hàm này trả về diện tích của hình chữ nhật hoặc hình vuông."""
    if chieu_rong is None:
        chieu_rong = chieu_dai  # Nếu không cung cấp chiều rộng, coi như là hình vuông
    return chieu_dai * chieu_rong

# Gọi hàm và lưu giá trị trả về
dien_tich = tinh_dien_tich_hinh_chu_nhat(5)
print("Diện tích của hình vuông là:", dien_tich)

# Hàm có thể có tham số tùy chọn và trả về nhiều giá trị
def tinh_dien_tich_va_chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong=None):
    """Hàm này trả về diện tích và chu vi của hình chữ nhật hoặc hình vuông."""
    if chieu_rong is None:
        chieu_rong = chieu_dai  # Nếu không cung cấp chiều rộng, coi như là hình vuông
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
    return dien_tich, chu_vi
# Gọi hàm và lưu giá trị trả về
dien_tich, chu_vi = tinh_dien_tich_va_chu_vi_hinh_chu_nhat(5)
print("Diện tích của hình vuông là:", dien_tich)

print("Chu vi của hình vuông là:", chu_vi)



# Built-in functions (Hàm tích hợp sẵn)
# Hàm abs() trả về giá trị tuyệt đối của một số
print("Giá trị tuyệt đối của -5 là:", abs(-5))
# Hàm max() trả về giá trị lớn nhất trong một tập hợp
print("Giá trị lớn nhất trong [1, 2, 3, 4, 5] là:", max(1, 2, 3, 4, 5))
# Hàm min() trả về giá trị nhỏ nhất trong một tập hợp
print("Giá trị nhỏ nhất trong [1, 2, 3, 4, 5] là:", min(1, 2, 3, 4, 5))
# Hàm len() trả về độ dài của một chuỗi hoặc một tập hợp
print("Độ dài của chuỗi 'Hello' là:", len("Hello"))
# Hàm sum() trả về tổng của một tập hợp các số
print("Tổng của [1, 2, 3, 4, 5] là:", sum([1, 2, 3, 4, 5]))
# Hàm range() trả về một dãy số trong một khoảng nhất định
print("Dãy số từ 0 đến 9 là:", list(range(10)))
# Hàm type() trả về kiểu dữ liệu của một giá trị
print("Kiểu dữ liệu của 10 là:", type(10))
# Hàm str() chuyển đổi một giá trị thành chuỗi
print("Chuyển số 10 thành chuỗi:", str(10))
# Hàm int() chuyển đổi một giá trị thành số nguyên
print("Chuyển chuỗi '10' thành số nguyên:", int("10"))
# Hàm float() chuyển đổi một giá trị thành số thực
print("Chuyển chuỗi '3.14' thành số thực:", float("3.14"))
# Hàm input() cho phép người dùng nhập dữ liệu từ bàn phím
name = input("Nhập tên của bạn: ")
print("Chào mừng, " + name + "!")
# Hàm print() in Python có thể nhận nhiều đối số và tự động thêm dấu cách giữa chúng khi
# in ra màn hình
print("Xin chào", name, "!", "Hôm nay là một ngày đẹp trời.")

# Hàm có thể được định nghĩa bên trong một hàm khác (Nested functions)
def ham_ngoai():
    print("Đây là hàm ngoài.")
    
    def ham_trong():
        print("Đây là hàm trong.")
    
    ham_trong()
ham_ngoai()


# Hàm có thể được sử dụng như một đối tượng (First-class functions)
def ham_chao_mung(ten):
    print(f"Chào mừng, {ten}!") 
chao_mung = ham_chao_mung  # Gán hàm vào một biến khác
chao_mung("Bob")  # Gọi hàm thông qua biến mới

# Hàm có thể được sử dụng làm đối số cho hàm khác (Higher-order functions)
def ham_chao_mung(ten):
    print(f"Chào mừng, {ten}!")
def ham_goi_ham(h, ten):
    h(ten)  # Gọi hàm h với đối số ten
ham_goi_ham(ham_chao_mung, "Charlie")  # Truyền hàm chao_mung làm đối số

# Hàm có thể trả về một hàm khác (Closures)
def ham_tao_ham_chao_mung(ten):
    def ham_chao_mung():
        print(f"Chào mừng, {ten}!")
    return ham_chao_mung  # Trả về hàm chao_mung
ham_chao_mung_cho_alice = ham_tao_ham_chao_mung("Alice")  # Tạo một hàm chào mừng cho Alice
ham_chao_mung_cho_alice()  # Gọi hàm chào mừng cho Alice


# Hàm có thể có tham số tùy chọn và trả về nhiều giá trị
def tinh_dien_tich_va_chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong=None):
    """Hàm này trả về diện tích và chu vi của hình chữ nhật hoặc hình vuông."""
    if chieu_rong is None:
        chieu_rong = chieu_dai  # Nếu không cung cấp chiều rộng, coi như là hình vuông
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
    return dien_tich, chu_vi
# Gọi hàm và lưu giá trị trả về
dien_tich, chu_vi = tinh_dien_tich_va_chu_vi_hinh_chu_nhat(5)
print("Diện tích của hình vuông là:", dien_tich)
print("Chu vi của hình vuông là:", chu_vi)

