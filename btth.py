class BistroTable:
    _vat_rate = 0.08

    def __init__(self, table_id, capacity):
        self.__table_id = table_id.upper()
        self.__capacity = capacity
        self.__current_bill = 0

    @property
    def table_id(self):
        return self.__table_id

    @property
    def status(self):
        return "Có khách (Occupied)" if self.__current_bill > 0 else "Đang trống (Available)"

    @property
    def total_to_pay(self):
        return self.__current_bill * (1 + BistroTable._vat_rate)

    def order_dish(self, amount):
        if amount <= 0:
            return False
        self.__current_bill += amount
        return True

    def cancel_dish(self, amount):
        if amount <= 0 or amount > self.__current_bill:
            return False
        self.__current_bill -= amount
        return True

    def reset_table(self):
        self.__current_bill = 0

    @classmethod
    def update_vat(cls, new_rate):
        if 0 <= new_rate <= 0.2:
            cls._vat_rate = new_rate
            return True
        return False

    @staticmethod
    def validate_table_id(table_id):
        return isinstance(table_id, str) and table_id.upper().startswith("TB") and len(table_id) >= 3

def main():
    tables = [BistroTable("TB01", 4), BistroTable("TB02", 2), BistroTable("TB03", 8)]

    while True:
        print("\n===== HỆ THỐNG ĐIỀU PHỐI BÀN ĂN - RIKKEI BISTRO =====")
        print("1. Hiển thị sơ đồ & Trạng thái bàn ăn")
        print("2. Gọi món mới")
        print("3. Hủy món / Giảm trừ hóa đơn")
        print("4. Cập nhật thuế suất VAT")
        print("5. Thanh toán hóa đơn & Trả bàn trống")
        print("6. Thoát chương trình")
        
        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            print("\n--- SƠ ĐỒ BÀN ĂN RIKKEI BISTRO ---")
            for idx, t in enumerate(tables, 1):
                print(f"{idx}. Mã bàn: {t.table_id} | Sức chứa: {t._BistroTable__capacity} người | Tạm tính: {t._BistroTable__current_bill:,.0f}đ | Trạng thái: {t.status}")
            print("-" * 34)

        elif choice == "2":
            tid = input("Nhập mã bàn gọi món: ").upper()
            target = next((t for t in tables if t.table_id == tid), None)
            if not target:
                print(">> Lỗi: Không tìm thấy bàn!")
            else:
                try:
                    val = float(input("Nhập giá tiền món ăn: "))
                    if target.order_dish(val):
                        print(f">> Thành công: Đã ghi nhận {val:,.0f}đ vào {tid}.")
                    else:
                        print(">> Lỗi: Số tiền phải lớn hơn 0!")
                except ValueError:
                    print(">> Lỗi: Vui lòng nhập số hợp lệ!")

        elif choice == "3":
            tid = input("Nhập mã bàn cần hủy món: ").upper()
            target = next((t for t in tables if t.table_id == tid), None)
            if not target:
                print(">> Lỗi: Không tìm thấy bàn!")
            else:
                try:
                    val = float(input("Nhập giá trị giảm trừ: "))
                    if target.cancel_dish(val):
                        print(f">> Thành công: Đã giảm {val:,.0f}đ.")
                    else:
                        print(">> Lỗi: Số tiền không hợp lệ hoặc vượt quá hóa đơn!")
                except ValueError:
                    print(">> Lỗi: Vui lòng nhập số hợp lệ!")

        elif choice == "4":
            print(f"[HỆ THỐNG] VAT hiện tại: {BistroTable._vat_rate * 100:.0f}%")
            try:
                new_vat = float(input("Nhập VAT mới (0.0 - 0.2): "))
                if BistroTable.update_vat(new_vat):
                    print(f">> Thành công: Đã cập nhật VAT lên {new_vat*100:.0f}%")
                else:
                    print(">> Lỗi: Tỷ lệ không hợp lệ!")
            except ValueError:
                print(">> Lỗi: Nhập số thực!")

        elif choice == "5":
            tid = input("Nhập mã bàn thanh toán: ").upper()
            target = next((t for t in tables if t.table_id == tid), None)
            if not target:
                print(">> Lỗi: Không tìm thấy bàn!")
            elif target._BistroTable__current_bill == 0:
                print(">> Lỗi: Bàn đang trống!")
            else:
                print(f"\n--- HÓA ĐƠN {tid} ---")
                print(f"Tạm tính: {target._BistroTable__current_bill:,.0f}đ")
                print(f"VAT: {BistroTable._vat_rate*100:.0f}%")
                print(f"Tổng: {target.total_to_pay:,.0f}đ")
                target.reset_table()
                print(">> Thanh toán thành công!")

        elif choice == "6":
            print("Cảm ơn đã sử dụng!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()