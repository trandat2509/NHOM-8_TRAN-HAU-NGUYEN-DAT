# Định nghĩa class Node để biểu diễn một nút trong cây.
class Node:
    def __init__(self, value):
        # Thuộc tính 'value' lưu giá trị của nút.
        self.value = value
        # Thuộc tính 'children' lưu danh sách các nút con của nút hiện tại.
        self.children = []

# Hàm để nhập cây từ bàn phím.
def input_tree():
    # Nhập số lượng nút trong cây.
    n = int(input("Nhập số nút của cây: "))
    # Khởi tạo danh sách các nút rỗng.
    nodes = [None] * n
    # Nhập giá trị của các nút và lưu chúng vào danh sách nút.
    for i in range(n):
        val = int(input(f"Nhập giá trị của nút thứ {i + 1}: "))
        nodes[i] = Node(val)

    # Nhập các cạnh nối giữa các nút trong cây.
    for i in range(n - 1):
        # Nhập cạnh nối giữa hai nút 'u' và 'v'.
        u, v = map(int, input(f"Nhập cạnh nối giữa hai nút (u, v) trong khoảng từ 1 đến {n}: ").split())
        # Thêm nút 'v' vào danh sách nút con của nút 'u'.
        nodes[u - 1].children.append(nodes[v - 1])

    # Trả về nút gốc của cây.
    return nodes[0]

# Duyệt cây theo thứ tự trước (preorder traversal) và in giá trị của các nút theo thứ tự đó.
def preorder_traversal(node):
    # In giá trị của nút hiện tại.
    print(node.value, end=" ")
    # Duyệt các nút con của nút hiện tại.
    for child in node.children:
        preorder_traversal(child)

def main():
    # Nhập cây.
    root = input_tree()

    # Duyệt cây theo thứ tự trước và in ra giá trị
    print("Duyệt cây theo thứ tự trước: ")
    preorder_traversal(root)

if __name__ == "__main__":
    main()
