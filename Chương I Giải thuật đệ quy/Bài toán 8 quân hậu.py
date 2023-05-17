# Kích thước của bàn cờ
KICHTHUOCBANCO = 8

# In ra màn hình bàn cờ hiện tại
def in_ban_co(ban_co):
    for hang in range(KICHTHUOCBANCO):
        for cot in range(KICHTHUOCBANCO):
            print(ban_co[hang][cot], end=" ")
        print()

# Đặt quân hậu vào hàng hiện tại và kiểm tra nếu an toàn thì đệ quy tiếp tục đặt quân hậu vào hàng tiếp theo
def xep_hau(ban_co, hang):
    # Nếu đã đặt quân hậu vào hết các hàng thì in bàn cờ hiện tại và trả về
    if hang == KICHTHUOCBANCO:
        in_ban_co(ban_co)
        print()
        return
    # Nếu chưa đặt hết quân hậu, thử đặt quân hậu vào từng cột trong hàng hiện tại
    for cot in range(KICHTHUOCBANCO):
        # Kiểm tra nếu vị trí đó an toàn thì đặt quân hậu vào đó và đệ quy tiếp tục đặt quân hậu vào hàng tiếp theo
        if kiem_tra_vung_an_toan(ban_co, hang, cot):
            ban_co[hang][cot] = "Hậu"
            xep_hau(ban_co, hang + 1)
            # Sau khi đệ quy hoàn thành, bỏ quân hậu ra khỏi vị trí đó để thử với vị trí khác trong cùng hàng
            ban_co[hang][cot] = "-"

# Kiểm tra xem có quân hậu nào trên cùng cột hoặc đường chéo với vị trí đang xét không
def kiem_tra_vung_an_toan(ban_co, hang, cot):
    # Kiểm tra các hàng trước đó xem có quân hậu nào trên cùng cột không
    for i in range(hang):
        if ban_co[i][cot] == "Hậu":
            return False
        # Kiểm tra đường chéo chính của vị trí đang xét
        for j in range(KICHTHUOCBANCO):
            if ban_co[i][j] == "Hậu" and (hang - i == cot - j or hang - i == j - cot):
                return False
    # Nếu không có quân hậu nào trên cùng cột hoặc đường chéo thì vị trí đó an toàn
    return True

# Hàm chính để chạy chương trình
def main():
    # Tạo bàn cờ mới
    ban_co = [["-" for i in range(KICHTHUOCBANCO)] for j in range(KICHTHUOCBANCO)]
    # Đặt quân hậu vào hàng đầu tiên
    xep_hau(ban_co, 0)

# Chạy hàm chính
if __name__ == '__main__':
    main()

