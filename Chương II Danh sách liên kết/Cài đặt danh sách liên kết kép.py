# Tạo class Node
class DoublyLinkedListNode:
    # Hàm tạo Node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Tạo class List
class DoublyLinkedList:
    # Hàm tạo object danh sách liên kết
    def __init__(self):
        self.head = None

    # Hàm thêm node vào đầu danh sách
    def insert_at_beginning(self, data):
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Hàm thêm node vào cuối danh sách
    def insert_at_end(self, data):
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Hàm tìm kiếm node theo giá trị
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    # Hàm chèn node vào sau giá trị
    def insert_after(self, data, new_data):
        new_node = DoublyLinkedListNode(new_data)
        current = self.head
        while current is not None:
            if current.data == data:
                new_node.next = current.next
                new_node.prev = current
                if current.next is not None:
                    current.next.prev = new_node
                current.next = new_node
                return True
            current = current.next
        return False

    # Hàm xóa node
    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                    if current.next is not None:
                        current.next.prev = None
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                return True
            current = current.next
        return False

    # Hàm in ra danh sách kết quả
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# Tạo danh sách liên kết
linked_list = DoublyLinkedList()

# Nhập dữ liệu vào danh sách từ bàn phím
n = int(input("Nhập số lượng nút trong danh sách: "))
for i in range(n):
    data = str(input("Nhập giá trị của nút thứ " + str(i+1) + ": "))
    linked_list.insert_at_end(data)

# In danh sách liên kết ra màn hình
print("Danh sách liên kết:")
linked_list.print_list()
print("-------------------")


# Tìm kiếm giá trị và in ra màn hình
search_data = str(input("Nhập giá trị cần tìm kiếm: "))
if linked_list.search(search_data):
    print("Giá trị", search_data, "được tìm thấy trong danh sách.")
else:
    print("Giá trị", search_data, "không tồn tại trong danh sách.")
print("-------------------")


# Chèn giá trị vào đầu danh sách
data = str(input("Nhập giá trị chèn vào đầu nút: "))
linked_list.insert_at_beginning(data)
print("Danh sách liên kết mới khi chèn vào đầu nút:")
linked_list.print_list()
print("-------------------")


# Chèn giá trị vào cuối danh sách
data = str(input("Nhập giá tri chèn vào cuối nút: "))
linked_list.insert_at_end(data)
print("Danh sách liên kết mới khi chèn vào cuối nút:")
linked_list.print_list()
print("-------------------")


# chèn giá trị mới vào danh sách liên kết
insert_after_data = str(input("Nhập giá trị của nút muốn chèn vào sau nó: "))
new_data = str(input("Nhập giá trị mới muốn chèn vào: "))
if linked_list.insert_after(insert_after_data, new_data):
    print("Chèn giá trị", new_data, "sau nút có giá trị", insert_after_data, "thành công.")
else:
    print("Không tìm thấy nút có giá trị", insert_after_data, "trong danh sách.")

# in danh sách liên kết sau khi chèn giá trị mới
print("Danh sách liên kết sau khi chèn giá trị mới:")
linked_list.print_list()
print("-------------------")


# xóa một nút trong danh sách liên kết
delete_data = str(input("Nhập giá trị của nút muốn xóa: "))
if linked_list.delete(delete_data):
    print("Xóa nút có giá trị", delete_data, "thành công.")
else:
    print("Không tìm thấy nút có giá trị", delete_data, "trong danh sách.")

# in danh sách liên kết sau khi xóa nút
print("Danh sách liên kết sau khi xóa nút:")
linked_list.print_list()
