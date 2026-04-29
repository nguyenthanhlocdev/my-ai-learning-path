from pathlib import Path


def in_tieu_de(tieu_de):
    print(f"\n{'=' * 20} {tieu_de} {'=' * 20}")


def vi_du_range():
    in_tieu_de("1. Vi du range()")

    print("range(5):", list(range(5)))
    print("range(1, 6):", list(range(1, 6)))
    print("range(0, 11, 2):", list(range(0, 11, 2)))

    print("\nLap 5 lan ma khong can bien dem:")
    for _ in range(5):
        print("Hello Python")


def vi_du_tinh_tong():
    in_tieu_de("2. Co che cap nhat bien")

    total = 0
    for i in range(1, 6):
        total = total + i
        print(f"Sau khi cong {i}, total = {total}")

    print("Tong tu 1 den 5 =", total)


def vi_du_tinh_tong_chan():
    in_tieu_de("3. Tong cac so chan tu 0 den 10")

    tong_chan = 0
    for i in range(0, 11, 2):
        tong_chan += i
        print(f"Cong them {i}, tong_chan = {tong_chan}")

    print("Ket qua cuoi cung =", tong_chan)


def tinh_giai_thua(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f"i = {i}, result = {result}")
    return result


def vi_du_giai_thua():
    in_tieu_de("4. Tinh giai thua")

    n = 5
    ket_qua = tinh_giai_thua(n)
    print(f"{n}! = {ket_qua}")


def vi_du_break():
    in_tieu_de("5. break")

    danh_sach_nhan_vien = ["An", "Binh", "Chi", "Dung", "Hanh"]
    can_tim = "Chi"

    for ten in danh_sach_nhan_vien:
        print("Dang kiem tra:", ten)
        if ten == can_tim:
            print("Da tim thay nhan vien can tim.")
            break


def vi_du_vi_tri_print_voi_break():
    in_tieu_de("6. Vi tri cua print voi break")

    print("Dat print truoc break:")
    for i in range(1, 6):
        if i == 3:
            print("Tim thay so 3")
            break

    print("\nDat print sau break:")
    for i in range(1, 6):
        if i == 3:
            break
            print("Dong nay khong bao gio chay")

    print("Vong lap da ket thuc.")


def vi_du_continue():
    in_tieu_de("7. continue")

    danh_sach_nhan_vien = [
        ("An", True),
        ("Binh", False),
        ("Chi", True),
        ("Dung", False),
    ]

    for ten, du_dieu_kien in danh_sach_nhan_vien:
        if not du_dieu_kien:
            print(f"Bo qua {ten} vi khong du dieu kien.")
            continue

        print(f"Tang luong cho {ten}.")


def tinh_pi(so_vong_lap):
    tong = 0
    for i in range(1, so_vong_lap + 1):
        tong += ((-1) ** (i + 1)) / (2 * i - 1)
    return 4 * tong


def vi_du_tinh_pi():
    in_tieu_de("8. Xap xi so Pi")

    for so_vong_lap in [10, 100, 1000]:
        gia_tri_pi = tinh_pi(so_vong_lap)
        print(f"So vong lap = {so_vong_lap:4} -> pi ~= {gia_tri_pi}")


def can_bac_hai_newton(a, so_vong_lap=10):
    x = a / 2
    print(f"Gia tri doan ban dau x = {x}")

    for lan_lap in range(1, so_vong_lap + 1):
        x = (x + a / x) / 2
        print(f"Lan lap {lan_lap:2}: x = {x}")

    return x


def vi_du_can_bac_hai():
    in_tieu_de("9. Can bac hai bang Newton")

    a = 25
    ket_qua = can_bac_hai_newton(a)
    print(f"Can bac hai cua {a} ~= {ket_qua}")


def vi_du_while():
    in_tieu_de("10. while")

    dem = 1
    while dem <= 5:
        print(f"Lan lap thu {dem}")
        dem += 1


def vi_du_while_true():
    in_tieu_de("11. while True co break")

    lan_doc_cam_bien = 0
    while True:
        lan_doc_cam_bien += 1
        print(f"He thong dang doc du lieu lan {lan_doc_cam_bien}")

        if lan_doc_cam_bien == 3:
            print("Dung demo de tranh vong lap vo han.")
            break


def vi_du_file():
    in_tieu_de("12. Thao tac file")

    duong_dan_file = Path(__file__).with_name("demo_loop_output.txt")

    file = open(duong_dan_file, "w", encoding="utf-8")
    file.write("Dong 1: Hoc vong lap\n")
    file.write("Dong 2: Hoc thao tac file\n")
    file.close()
    print("Da ghi file:", duong_dan_file.name)

    file = open(duong_dan_file, "r", encoding="utf-8")
    noi_dung = file.read()
    file.close()

    print("Noi dung vua doc duoc:")
    print(noi_dung)


def main():
    vi_du_range()
    vi_du_tinh_tong()
    vi_du_tinh_tong_chan()
    vi_du_giai_thua()
    vi_du_break()
    vi_du_vi_tri_print_voi_break()
    vi_du_continue()
    vi_du_tinh_pi()
    vi_du_can_bac_hai()
    vi_du_while()
    vi_du_while_true()
    vi_du_file()


if __name__ == "__main__":
    main()
