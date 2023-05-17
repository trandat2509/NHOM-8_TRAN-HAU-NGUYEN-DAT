def is_valid_move(x, y, visited, n):
    """
    Kiểm tra nước đi có hợp lệ hay không
    """
    if x >= 0 and y >= 0 and x < n and y < n and visited[x][y] == -1:
        return True
    return False

def knight_tour(x, y, visited, n, move_num):
    """
    Tìm kiếm các nước đi của quân mã
    """
    if move_num == n*n:
        return True

    # Các bước di chuyển có thể của quân mã
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    # Thử từng nước đi
    for i in range(8):
        next_x = x + x_moves[i]
        next_y = y + y_moves[i]
        if is_valid_move(next_x, next_y, visited, n):
            visited[next_x][next_y] = move_num
            if knight_tour(next_x, next_y, visited, n, move_num+1):
                return True
            visited[next_x][next_y] = -1

    return False

def main():
    n = 8  # Kích thước của bàn cờ
    visited = [[-1 for i in range(n)] for j in range(n)]  # Ma trận đánh dấu các ô đã đi qua

    # Đặt quân mã vào ô đầu tiên
    visited[0][0] = 0
    if knight_tour(0, 0, visited, n, 1):
        # In ra các bước di chuyển
        for i in range(n):
            for j in range(n):
                print(visited[i][j], end=" ")
            print()
    else:
        print("Không tìm thấy giải pháp")

if __name__ == "__main__":
    main()
