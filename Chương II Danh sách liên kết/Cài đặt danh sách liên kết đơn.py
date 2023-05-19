# Node class
class Node:

    # Hàm tạo node
    def __init__(self, data):
        self.data = data  # Gán dữ liệu
        self.next = None  # Thuộc tính next trỏ đến nút tiếp theo
        # next mặc định là None


# Linked List class
class LinkedList:

    # Hàm tạo object danh sách liên kết
    def __init__(self):
        self.head = None

    # Hàm in nội dung danh sách liên kết bắt đầu từ node đầu (head)
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Hàm thêm node vào đầu danh sách
    def addAtBeginning(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    # Hàm thêm node vào cuối danh sách
    def addAtEnd(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode

    # Hàm tìm kiếm node theo giá trị
    def searchNode(self, value):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == value:
                print('Giá trị ' f"{value} được tìm thấy trong danh sách")
                return curr_node
            curr_node = curr_node.next
        print("Giá trị " f"{value} không được tìm thấy trong danh sách")

    # Hàm thêm node vào giữa 2 node có sẵn trong danh sách
    def addAfterNode(self, insert_after_data, new_data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == insert_after_data:
                new_node = Node(new_data)
                new_node.next = curr_node.next
                curr_node.next = new_node
                return
            curr_node = curr_node.next
        print("Không tìm thấy nút có giá trị", insert_after_data, "trong danh sách.")

    # Hàm xóa 1 node theo giá trị
    def removeNode(self, value):
        head_val = self.head
        if head_val is not None:
            if head_val.data == value:
                self.head = head_val.next
                head_val.data = None
                return
        while head_val is not None: 
            if head_val.data == value:
                break
            prev = head_val
            head_val = head_val.next
        if head_val is None:
            return
        prev.next = head_val.next
        head_val = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        print()
    
#Tạo danh sách liên kết
llist = LinkedList()

#Nhập dữ liệu vào danh sách từ bàn phím
n = int(input("Nhập số lượng nút trong danh sách: "))
for i in range(n):
    data = str(input("Nhập giá trị của nút thứ " + str(i+1) + ': '))
    llist.addAtEnd(data)

# In danh sách liên kết ra màn hình
print("Danh sách liên kết: ")
llist.printList()
print('----------')

# Tìm kiếm giá trị và in ra màn hình
search = str(input("Nhập giá trị cần tìm kiếm: "))
llist.searchNode(search)
print('----------')

# Chèn giá trị vào đầu 
begin = str(input("Nhập giá trị cần chèn vào đầu: "))
llist.addAtBeginning(begin)
llist.printList()
print('----------')

# Chèn giá trị vào cuối
end = str(input("Nhập giá trị cần chèn vào cuối: "))
llist.addAtEnd(end)
llist.printList()
print('----------')

# Thêm một nút mới vào danh sách liên kết
insert_after_data = str(input("Nhập giá trị của nút muốn chèn vào sau nó: "))
new_data = str(input("Nhập giá trị mới muốn chèn vào: "))
llist.addAfterNode(insert_after_data, new_data)

# In danh sách liên kết sau khi thêm nút mới
print("Danh sách liên kết sau khi chèn:")
llist.printList()
print('----------')

# Xóa một nút trong danh sách
delete = str(input('Nhập giá trị cần xóa: '))
llist.removeNode(delete)
llist.printList()
print("Đã xóa thành công")
