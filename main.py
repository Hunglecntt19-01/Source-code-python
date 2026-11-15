# -*- coding: utf-8 -*-
"""
BÀI TẬP LỚN HỌC PHẦN: LẬP TRÌNH PYTHON
ĐỀ TÀI SỐ 22: XÂY DỰNG CHƯƠNG TRÌNH QUẢN LÝ DANH SÁCH KHÁCH HÀNG CỦA CÔNG TY
Sinh viên thực hiện: Lê Văn Hưng
Trường: Đại học Đại Nam
"""

import os
import sys

# Cấu hình mã hóa UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_DEFAULT = os.path.join(BASE_DIR, "data_customers.txt")


def xac_dinh_hang_khach_hang(tong_chi_tieu, so_lan_mua):
    """
    Quy tắc xếp hạng khách hàng:
    - Kim Cương: Tổng chi tiêu >= 50.000.000 VNĐ và Số lần mua >= 10
    - Vàng:      Tổng chi tiêu >= 20.000.000 VNĐ và Số lần mua >= 5
    - Bạc:       Tổng chi tiêu >= 5.000.000 VNĐ
    - Đồng:      Các trường hợp còn lại
    """
    if tong_chi_tieu >= 50000000 and so_lan_mua >= 10:
        return "Kim Cương"
    elif tong_chi_tieu >= 20000000 and so_lan_mua >= 5:
        return "Vàng"
    elif tong_chi_tieu >= 5000000:
        return "Bạc"
    else:
        return "Đồng"


def kiem_tra_ma_trung(danh_sach, ma_kh):
    """Kiểm tra mã khách hàng đã tồn tại trong danh sách hay chưa (không phân biệt hoa thường)."""
    ma_chuan = ma_kh.strip().upper()
    for kh in danh_sach:
        if kh["ma_kh"].strip().upper() == ma_chuan:
            return True
    return False


def them_khach_hang(danh_sach):
    """Chức năng 1: Thêm khách hàng mới vào hệ thống."""
    print("\n--- THÊM MỚI KHÁCH HÀNG ---")
    while True:
        ma_kh = input("Nhập mã khách hàng (VD: KH020, nhấn Enter để hủy): ").strip().upper()
        if not ma_kh:
            print(">> Đã hủy thao tác thêm khách hàng.")
            return
        if kiem_tra_ma_trung(danh_sach, ma_kh):
            print(f"[LỖI] Mã khách hàng '{ma_kh}' đã tồn tại! Vui lòng nhập mã khác.")
            continue
        break

    while True:
        ho_ten = input("Nhập họ và tên: ").strip()
        if not ho_ten:
            print("[LỖI] Họ tên không được để trống!")
            continue
        break

    while True:
        sdt = input("Nhập số điện thoại (10 chữ số, bắt đầu bằng 0): ").strip()
        if not (sdt.isdigit() and len(sdt) == 10 and sdt.startswith("0")):
            print("[LỖI] Số điện thoại không hợp lệ! Vui lòng nhập đúng 10 số (bắt đầu bằng 0).")
            continue
        break

    while True:
        email = input("Nhập địa chỉ email: ").strip()
        if not ("@" in email and "." in email and not email.startswith("@")):
            print("[LỖI] Email không đúng định dạng (VD: example@gmail.com)!")
            continue
        break

    dia_chi = input("Nhập địa chỉ: ").strip()
    if not dia_chi:
        dia_chi = "Chưa cập nhật"

    print("Chọn loại khách hàng:")
    print("  1. Cá nhân")
    print("  2. Doanh nghiệp")
    loai_chon = input("Lựa chọn (1 hoặc 2, mặc định 1): ").strip()
    loai_kh = "Doanh nghiệp" if loai_chon == "2" else "Cá nhân"

    while True:
        try:
            tong_chi_tieu_str = input("Nhập tổng giá trị mua hàng (VNĐ, >= 0): ").strip()
            tong_chi_tieu = float(tong_chi_tieu_str)
            if tong_chi_tieu < 0:
                print("[LỖI] Tổng giá trị mua hàng không được âm!")
                continue
            break
        except ValueError:
            print("[LỖI] Giá trị mua hàng phải là số hợp lệ!")

    while True:
        try:
            so_lan_mua_str = input("Nhập số lần mua hàng (>= 0): ").strip()
            so_lan_mua = int(so_lan_mua_str)
            if so_lan_mua < 0:
                print("[LỖI] Số lần mua không được âm!")
                continue
            break
        except ValueError:
            print("[LỖI] Số lần mua phải là số nguyên!")

    hang_kh = xac_dinh_hang_khach_hang(tong_chi_tieu, so_lan_mua)

    kh_moi = {
        "ma_kh": ma_kh,
        "ho_ten": ho_ten,
        "sdt": sdt,
        "email": email,
        "dia_chi": dia_chi,
        "loai_kh": loai_kh,
        "tong_chi_tieu": tong_chi_tieu,
        "so_lan_mua": so_lan_mua,
        "hang_kh": hang_kh
    }

    danh_sach.append(kh_moi)
    print(f"[THÀNH CÔNG] Đã thêm khách hàng '{ho_ten}' (Mã: {ma_kh}) - Phân hạng: {hang_kh}!")


def in_dong_khach_hang(stt, kh):
    """In định dạng một hàng thông tin khách hàng."""
    gia_tri_tb = kh["tong_chi_tieu"] / kh["so_lan_mua"] if kh["so_lan_mua"] > 0 else 0.0
    print(f"| {stt:<3} | {kh['ma_kh']:<7} | {kh['ho_ten']:<25} | {kh['sdt']:<11} | {kh['loai_kh']:<12} | "
          f"{kh['tong_chi_tieu']:>14,.0f} | {kh['so_lan_mua']:>6} | {gia_tri_tb:>14,.0f} | {kh['hang_kh']:<10} |")


def hien_thi_danh_sach(danh_sach, tieu_de="DANH SÁCH KHÁCH HÀNG CỦA CÔNG TY"):
    """Chức năng 2: Hiển thị danh sách khách hàng dưới dạng bảng có kẻ ô."""
    if not danh_sach:
        print("\n>> Danh sách khách hàng hiện đang trống!")
        return

    print(f"\n====================================================== {tieu_de} ======================================================")
    duong_ke = "+-----+---------+---------------------------+-------------+--------------+----------------+--------+----------------+------------+"
    print(duong_ke)
    print(f"| {'STT':<3} | {'Mã KH':<7} | {'Họ và tên':<25} | {'Điện thoại':<11} | {'Phân loại':<12} | {'Tổng chi (VNĐ)':>14} | {'Số lần':>6} | {'TB/Lần (VNĐ)':>14} | {'Hạng KH':<10} |")
    print(duong_ke)

    for idx, kh in enumerate(danh_sach, start=1):
        in_dong_khach_hang(idx, kh)

    print(duong_ke)
    print(f">> Tổng cộng hiển thị: {len(danh_sach)} khách hàng.\n")


def cap_nhat_khach_hang(danh_sach):
    """Chức năng 3: Cập nhật thông tin khách hàng theo mã định danh."""
    print("\n--- CẬP NHẬT THÔNG TIN KHÁCH HÀNG ---")
    ma_kh = input("Nhập mã khách hàng cần cập nhật: ").strip().upper()

    kh_tim_thay = None
    for kh in danh_sach:
        if kh["ma_kh"].upper() == ma_kh:
            kh_tim_thay = kh
            break

    if not kh_tim_thay:
        print(f"[LỖI] Không tìm thấy khách hàng có mã '{ma_kh}'!")
        return

    print(f"\nĐang cập nhật khách hàng: {kh_tim_thay['ho_ten']} ({kh_tim_thay['ma_kh']})")
    print("(Nhấn Enter để giữ nguyên giá trị hiện tại)")

    ten_moi = input(f"Họ tên hiện tại [{kh_tim_thay['ho_ten']}]: ").strip()
    if ten_moi:
        kh_tim_thay["ho_ten"] = ten_moi

    while True:
        sdt_moi = input(f"Số điện thoại hiện tại [{kh_tim_thay['sdt']}]: ").strip()
        if not sdt_moi:
            break
        if sdt_moi.isdigit() and len(sdt_moi) == 10 and sdt_moi.startswith("0"):
            kh_tim_thay["sdt"] = sdt_moi
            break
        print("[LỖI] Số điện thoại phải gồm 10 chữ số bắt đầu bằng 0!")

    while True:
        email_moi = input(f"Email hiện tại [{kh_tim_thay['email']}]: ").strip()
        if not email_moi:
            break
        if "@" in email_moi and "." in email_moi:
            kh_tim_thay["email"] = email_moi
            break
        print("[LỖI] Email không đúng định dạng!")

    dia_chi_moi = input(f"Địa chỉ hiện tại [{kh_tim_thay['diaChi' if 'diaChi' in kh_tim_thay else 'dia_chi']}]: ").strip()
    if dia_chi_moi:
        kh_tim_thay["dia_chi"] = dia_chi_moi

    loai_moi = input(f"Loại khách hàng hiện tại [{kh_tim_thay['loai_kh']}] (1: Cá nhân, 2: Doanh nghiệp): ").strip()
    if loai_moi == "1":
        kh_tim_thay["loai_kh"] = "Cá nhân"
    elif loai_moi == "2":
        kh_tim_thay["loai_kh"] = "Doanh nghiệp"

    while True:
        tien_moi = input(f"Tổng chi tiêu hiện tại [{kh_tim_thay['tong_chi_tieu']:,.0f}]: ").strip()
        if not tien_moi:
            break
        try:
            val = float(tien_moi)
            if val < 0:
                print("[LỖI] Tiền không được âm!")
                continue
            kh_tim_thay["tong_chi_tieu"] = val
            break
        except ValueError:
            print("[LỖI] Phải nhập số hợp lệ!")

    while True:
        lan_moi = input(f"Số lần mua hiện tại [{kh_tim_thay['so_lan_mua']}]: ").strip()
        if not lan_moi:
            break
        try:
            val = int(lan_moi)
            if val < 0:
                print("[LỖI] Số lần mua không được âm!")
                continue
            kh_tim_thay["so_lan_mua"] = val
            break
        except ValueError:
            print("[LỖI] Phải nhập số nguyên!")

    # Cập nhật lại hạng sau khi sửa chi tiêu hoặc số lần mua
    kh_tim_thay["hang_kh"] = xac_dinh_hang_khach_hang(kh_tim_thay["tong_chi_tieu"], kh_tim_thay["so_lan_mua"])
    print(f"[THÀNH CÔNG] Đã cập nhật thông tin khách hàng '{kh_tim_thay['ma_kh']}' thành công! Hạng mới: {kh_tim_thay['hang_kh']}")


def xoa_khach_hang(danh_sach):
    """Chức năng 4: Xóa khách hàng với yêu cầu xác nhận."""
    print("\n--- XÓA KHÁCH HÀNG ---")
    ma_kh = input("Nhập mã khách hàng cần xóa: ").strip().upper()

    vi_tri = -1
    for idx, kh in enumerate(danh_sach):
        if kh["ma_kh"].upper() == ma_kh:
            vi_tri = idx
            break

    if vi_tri == -1:
        print(f"[LỖI] Không tìm thấy khách hàng có mã '{ma_kh}'!")
        return

    kh = danh_sach[vi_tri]
    print(f"CẢNH BÁO: Bạn sắp xóa khách hàng: {kh['ho_ten']} - Mã: {kh['ma_kh']} - Hạng: {kh['hang_kh']}")
    xac_nhan = input("Bạn có chắc chắn muốn xóa không? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        danh_sach.pop(vi_tri)
        print(f"[THÀNH CÔNG] Đã xóa vĩnh viễn khách hàng '{ma_kh}' khỏi hệ thống!")
    else:
        print(">> Đã hủy bỏ thao tác xóa.")


def tim_kiem_khach_hang(danh_sach):
    """Chức năng 5: Tìm kiếm khách hàng theo Mã, Họ tên hoặc Số điện thoại."""
    print("\n--- TÌM KIẾM KHÁCH HÀNG ---")
    print("1. Tìm kiếm theo Mã khách hàng")
    print("2. Tìm kiếm theo Họ và tên")
    print("3. Tìm kiếm theo Số điện thoại")
    lua_chon = input("Chọn tiêu chí tìm kiếm (1-3): ").strip()

    ket_qua = []
    if lua_chon == "1":
        tu_khoa = input("Nhập mã khách hàng cần tìm: ").strip().upper()
        ket_qua = [kh for kh in danh_sach if tu_khoa in kh["ma_kh"].upper()]
    elif lua_chon == "2":
        tu_khoa = input("Nhập tên khách hàng cần tìm: ").strip().lower()
        ket_qua = [kh for kh in danh_sach if tu_khoa in kh["ho_ten"].lower()]
    elif lua_chon == "3":
        tu_khoa = input("Nhập số điện thoại cần tìm: ").strip()
        ket_qua = [kh for kh in danh_sach if tu_khoa in kh["sdt"]]
    else:
        print("[LỖI] Tiêu chí tìm kiếm không hợp lệ!")
        return

    if ket_qua:
        hien_thi_danh_sach(ket_qua, f"KẾT QUẢ TÌM KIẾM ({len(ket_qua)} KHÁCH HÀNG PHÙ HỢP)")
    else:
        print(f">> Không tìm thấy khách hàng nào khớp với từ khóa tìm kiếm!")


def sap_xep_khach_hang(danh_sach):
    """Chức năng 6: Sắp xếp theo họ tên hoặc tổng giá trị mua hàng."""
    if not danh_sach:
        print("\n>> Danh sách trống, không thể sắp xếp!")
        return

    print("\n--- SẮP XẾP DANH SÁCH KHÁCH HÀNG ---")
    print("1. Sắp xếp theo Họ và tên")
    print("2. Sắp xếp theo Tổng giá trị mua hàng")
    tieu_chi = input("Chọn tiêu chí sắp xếp (1 hoặc 2): ").strip()

    print("Chọn thứ tự:")
    print("1. Tăng dần (A-Z hoặc Thấp đến Cao)")
    print("2. Giảm dần (Z-A hoặc Cao đến Thấp)")
    thu_tu = input("Chọn thứ tự (1 hoặc 2): ").strip()
    is_reverse = (thu_tu == "2")

    if tieu_chi == "1":
        # Lấy tên (từ cuối cùng của họ tên) để sắp xếp chuẩn tiếng Việt
        danh_sach.sort(key=lambda x: x["ho_ten"].strip().split()[-1].lower(), reverse=is_reverse)
        huong = "giảm dần (Z-A)" if is_reverse else "tăng dần (A-Z)"
        print(f"[THÀNH CÔNG] Đã sắp xếp danh sách theo Họ tên {huong}!")
    elif tieu_chi == "2":
        danh_sach.sort(key=lambda x: x["tong_chi_tieu"], reverse=is_reverse)
        huong = "giảm dần (cao xuống thấp)" if is_reverse else "tăng dần (thấp lên cao)"
        print(f"[THÀNH CÔNG] Đã sắp xếp danh sách theo Tổng giá trị mua hàng {huong}!")
    else:
        print("[LỖI] Lựa chọn tiêu chí không hợp lệ!")
        return

    hien_thi_danh_sach(danh_sach, "DANH SÁCH SAU KHI SẮP XẾP")


def tinh_toan_thong_ke(danh_sach):
    """Chức năng 7: Thống kê và tính toán các chỉ số kinh doanh của khách hàng."""
    if not danh_sach:
        print("\n>> Danh sách trống, không có dữ liệu để thống kê!")
        return

    print("\n========================= BÁO CÁO THỐNG KÊ KINH DOANH =========================")
    tong_so_kh = len(danh_sach)
    tong_doanh_thu = sum(kh["tong_chi_tieu"] for kh in danh_sach)
    tong_luot_mua = sum(kh["so_lan_mua"] for kh in danh_sach)
    tb_doanh_thu_kh = tong_doanh_thu / tong_so_kh if tong_so_kh > 0 else 0
    tb_gia_tri_don = tong_doanh_thu / tong_luot_mua if tong_luot_mua > 0 else 0

    # Khách hàng có tổng giá trị mua cao nhất và thấp nhất
    kh_cao_nhat = max(danh_sach, key=lambda x: x["tong_chi_tieu"])
    kh_thap_nhat = min(danh_sach, key=lambda x: x["tong_chi_tieu"])

    # Khách hàng có giá trị trung bình mỗi lần mua cao nhất
    kh_tb_cao_nhat = max(
        danh_sach,
        key=lambda x: (x["tong_chi_tieu"] / x["so_lan_mua"]) if x["so_lan_mua"] > 0 else 0
    )
    val_tb_max = kh_tb_cao_nhat["tong_chi_tieu"] / kh_tb_cao_nhat["so_lan_mua"] if kh_tb_cao_nhat["so_lan_mua"] > 0 else 0

    # Thống kê theo phân hạng
    thong_ke_hang = {"Đồng": 0, "Bạc": 0, "Vàng": 0, "Kim Cương": 0}
    for kh in danh_sach:
        h = kh["hang_kh"]
        thong_ke_hang[h] = thong_ke_hang.get(h, 0) + 1

    # Thống kê theo loại khách hàng
    thong_ke_loai = {"Cá nhân": 0, "Doanh nghiệp": 0}
    for kh in danh_sach:
        l = kh["loai_kh"]
        thong_ke_loai[l] = thong_ke_loai.get(l, 0) + 1

    print(f"1. TỔNG QUAN:")
    print(f"   - Tổng số khách hàng quản lý:        {tong_so_kh:>15} khách hàng")
    print(f"   - Tổng doanh thu toàn hệ thống:      {tong_doanh_thu:>15,.0f} VNĐ")
    print(f"   - Tổng số lượt giao dịch mua:        {tong_luot_mua:>15} lượt")
    print(f"   - Doanh thu bình quân mỗi khách hàng:{tb_doanh_thu_kh:>15,.0f} VNĐ")
    print(f"   - Giá trị đơn hàng trung bình/lần:   {tb_gia_tri_don:>15,.0f} VNĐ")

    print(f"\n2. ĐIỂM SÁNG KHÁCH HÀNG:")
    print(f"   - Chi tiêu cao nhất:  {kh_cao_nhat['ho_ten']} ({kh_cao_nhat['ma_kh']}) -> {kh_cao_nhat['tong_chi_tieu']:,.0f} VNĐ ({kh_cao_nhat['hang_kh']})")
    print(f"   - Chi tiêu thấp nhất: {kh_thap_nhat['ho_ten']} ({kh_thap_nhat['ma_kh']}) -> {kh_thap_nhat['tong_chi_tieu']:,.0f} VNĐ ({kh_thap_nhat['hang_kh']})")
    print(f"   - Đơn hàng TB lớn nhất:{kh_tb_cao_nhat['ho_ten']} ({kh_tb_cao_nhat['ma_kh']}) -> {val_tb_max:,.0f} VNĐ/lần mua")

    print(f"\n3. CƠ CẤU THEO PHÂN HẠNG KHÁCH HÀNG:")
    for hang, sl in thong_ke_hang.items():
        tl = (sl / tong_so_kh) * 100 if tong_so_kh > 0 else 0
        print(f"   + Hạng {hang:<10}: {sl:>3} khách ({tl:>5.1f}%)")

    print(f"\n4. CƠ CẤU THEO LOẠI HÌNH:")
    for loai, sl in thong_ke_loai.items():
        tl = (sl / tong_so_kh) * 100 if tong_so_kh > 0 else 0
        print(f"   + Khách {loai:<12}: {sl:>3} khách ({tl:>5.1f}%)")
    print("===============================================================================\n")


def luu_file(danh_sach, duong_dan=DATA_FILE_DEFAULT):
    """Chức năng 8: Lưu danh sách khách hàng xuống file văn bản TXT."""
    try:
        with open(duong_dan, "w", encoding="utf-8") as f:
            for kh in danh_sach:
                dong = f"{kh['ma_kh']}|{kh['ho_ten']}|{kh['sdt']}|{kh['email']}|{kh['dia_chi']}|{kh['loai_kh']}|{kh['tong_chi_tieu']:.0f}|{kh['so_lan_mua']}|{kh['hang_kh']}\n"
                f.write(dong)
        print(f"[THÀNH CÔNG] Đã lưu an toàn {len(danh_sach)} khách hàng vào tệp '{duong_dan}'!")
        return True
    except Exception as e:
        print(f"[LỖI] Không thể lưu file '{duong_dan}': {e}")
        return False


def doc_file(duong_dan=DATA_FILE_DEFAULT):
    """Chức năng 9: Đọc dữ liệu từ file văn bản TXT và chuyển đổi kiểu dữ liệu."""
    if not os.path.exists(duong_dan):
        print(f"[CẢNH BÁO] Tệp dữ liệu '{duong_dan}' chưa tồn tại. Hệ thống khởi tạo danh sách trống!")
        return []

    danh_sach = []
    try:
        with open(duong_dan, "r", encoding="utf-8") as f:
            dong_so = 0
            for line in f:
                dong_so += 1
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) >= 8:
                    ma_kh = parts[0].strip()
                    ho_ten = parts[1].strip()
                    sdt = parts[2].strip()
                    email = parts[3].strip()
                    dia_chi = parts[4].strip()
                    loai_kh = parts[5].strip()
                    tong_chi_tieu = float(parts[6].strip())
                    so_lan_mua = int(parts[7].strip())
                    hang_kh = parts[8].strip() if len(parts) > 8 else xac_dinh_hang_khach_hang(tong_chi_tieu, so_lan_mua)

                    danh_sach.append({
                        "ma_kh": ma_kh,
                        "ho_ten": ho_ten,
                        "sdt": sdt,
                        "email": email,
                        "dia_chi": dia_chi,
                        "loai_kh": loai_kh,
                        "tong_chi_tieu": tong_chi_tieu,
                        "so_lan_mua": so_lan_mua,
                        "hang_kh": hang_kh
                    })
        print(f"[THÀNH CÔNG] Đã đọc thành công {len(danh_sach)} bản ghi khách hàng từ tệp '{duong_dan}'!")
        return danh_sach
    except Exception as e:
        print(f"[LỖI] Lỗi khi đọc file '{duong_dan}': {e}")
        return []


def hien_thi_menu():
    """In giao diện Menu chính chuẩn của Đề tài số 22."""
    print("==================================================================")
    print("  CHƯƠNG TRÌNH QUẢN LÝ DANH SÁCH KHÁCH HÀNG CÔNG TY - PYTHON 3.14  ")
    print("==================================================================")
    print("  1. Thêm khách hàng mới")
    print("  2. Hiển thị danh sách khách hàng")
    print("  3. Cập nhật thông tin khách hàng")
    print("  4. Xóa khách hàng")
    print("  5. Tìm kiếm khách hàng")
    print("  6. Sắp xếp khách hàng")
    print("  7. Tính toán / Báo cáo thống kê")
    print("  8. Lưu dữ liệu vào file TXT")
    print("  9. Đọc dữ liệu từ file TXT")
    print("  0. Thoát chương trình")
    print("==================================================================")


def main():
    """Hàm điều khiển luồng chính của chương trình."""
    print("Khởi động hệ thống Quản lý Khách hàng...")
    # Tự động đọc dữ liệu khi khởi động
    danh_sach_kh = doc_file(DATA_FILE_DEFAULT)

    while True:
        hien_thi_menu()
        chon = input("Vui lòng chọn chức năng [0-9]: ").strip()

        if chon == "1":
            them_khach_hang(danh_sach_kh)
        elif chon == "2":
            hien_thi_danh_sach(danh_sach_kh)
        elif chon == "3":
            cap_nhat_khach_hang(danh_sach_kh)
        elif chon == "4":
            xoa_khach_hang(danh_sach_kh)
        elif chon == "5":
            tim_kiem_khach_hang(danh_sach_kh)
        elif chon == "6":
            sap_xep_khach_hang(danh_sach_kh)
        elif chon == "7":
            tinh_toan_thong_ke(danh_sach_kh)
        elif chon == "8":
            luu_file(danh_sach_kh, DATA_FILE_DEFAULT)
        elif chon == "9":
            danh_sach_kh = doc_file(DATA_FILE_DEFAULT)
        elif chon == "0":
            print("\nBạn có muốn tự động lưu dữ liệu trước khi thoát không? (Y/N): ", end="")
            luu_truoc_khi_thoat = input().strip().upper()
            if luu_truoc_khi_thoat == "Y":
                luu_file(danh_sach_kh, DATA_FILE_DEFAULT)
            print(">> Cảm ơn bạn đã sử dụng chương trình Quản lý Khách hàng! Tạm biệt.\n")
            break
        else:
            print("[CẢNH BÁO] Lựa chọn không hợp lệ! Vui lòng chọn từ 0 đến 9.\n")


if __name__ == "__main__":
    main()
