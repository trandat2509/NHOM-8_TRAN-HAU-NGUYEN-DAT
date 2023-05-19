# Khai báo lớp đại diện cho một đỉnh trong đồ thị
class Vertex: 
    def __init__(self, value): # Hàm khởi tạo của lớp
        self.value = value # Gán giá trị của tham số
        self.edges = []  # Danh sách các cạnh liên kết từ đỉnh này

# Khai báo lớp đại diện cho một cạnh trong đồ thị
class Edge:
    def __init__(self, source, destination): # Hàm khởi tạo của lớp
        self.source = source  # Đỉnh nguồn của cạnh
        self.destination = destination  # Đỉnh đích của cạnh

# Khai báo lớp đại diện cho cấu trúc dữ liệu đồ thị
class Graph:
    def __init__(self): # Hàm khởi tạo của lớp
        self.vertices = {}  # Lưu trữ các đỉnh của đồ thị và danh sách các cạnh kề

    def add_vertex(self, value): # Hàm thêm một đỉnh mới vào đồ thị
        if value not in self.vertices: # Kiểm tra xem đỉnh có tồn tại trong đồ thị hay không
            vertex = Vertex(value) # Tạo đối tượng đỉnh mới
            self.vertices[value] = vertex  # Thêm một đỉnh mới vào đồ thị

    def add_edge(self, source, destination): # Hàm thêm một cạnh mới vào đồ thị
        if source in self.vertices and destination in self.vertices: # Kiểm tra xem cả đỉnh nguồn và đỉnh đích có tồn tại trong đồ thị hay không.
            edge = Edge(self.vertices[source], self.vertices[destination]) # Tạo một cạnh mới
            self.vertices[source].edges.append(edge)  # Thêm một cạnh từ đỉnh nguồn đến đỉnh đích

    def remove_vertex(self, value): # Hàm xóa một đỉnh khỏi đồ thị
        if value in self.vertices: # Kiểm tra xem đỉnh có tồn tại trong đồ thị hay không
            vertex = self.vertices[value] 
            for v in self.vertices.values(): # Lặp qua các đỉnh trong đồ thị
                v.edges = [e for e in v.edges if e.destination != vertex]  # Xóa các cạnh liên quan đến đỉnh
            del self.vertices[value]  # Xóa đỉnh khỏi đồ thị

    def remove_edge(self, source, destination): # Hàm xóa một cạnh khỏi đồ thị
        if source in self.vertices: # Kiểm tra xem cạnh có tồn tại trong đồ thị hay không
            edges = self.vertices[source].edges
            self.vertices[source].edges = [e for e in edges if e.destination != self.vertices[destination]]  # Xóa cạnh từ đỉnh nguồn đến đỉnh đích

    def print_graph(self):  # Hàm in đồ thị
        for vertex in self.vertices.values(): 
            for edge in vertex.edges:
                print(f"{edge.source.value} -> {edge.destination.value}")  # In đồ thị có hướng

    def breadth_first_search(self, start_vertex): # Khởi tạo hàm để duyệt đồ thị theo chiều rộng (BFS)
        visited = set() # Tập hợp rỗng lưu các đỉnh đã được duyệt
        queue = [start_vertex]

        while queue: # Vòng lặp cho đến khi hàng đợi rỗng
            current_vertex = queue.pop(0)
            if current_vertex not in visited: # Kiểm tra xem đỉnh hiện tại đã được duyệt hay chưa.
                print(current_vertex.value)
                visited.add(current_vertex)
                for edge in current_vertex.edges: #  Lặp qua danh sách các cạnh của đỉnh hiện tại.
                    queue.append(edge.destination)  # Thêm các đỉnh kề vào hàng đợi

    def depth_first_search(self, start_vertex): # Khởi tạo hàm để duyệt đồ thị theo chiều sâu (DFS)
        visited = set() 

        def dfs_helper(vertex): #  Định nghĩa hàm để thực hiện duyệt đồ thị theo chiều sâu từ một đỉnh cụ thể.
            print(vertex.value)
            visited.add(vertex)
            for edge in vertex.edges: # Lặp qua danh sách các cạnh của đỉnh hiện tại.
                if edge.destination not in visited: # Kiểm tra xem đỉnh đích của cạnh có trong tập hợp các đỉnh đã được duyệt hay chưa.
                    dfs_helper(edge.destination)  # Gọi đệ quy để duyệt các đỉnh kề chưa được thăm

        dfs_helper(start_vertex) # Gọi đệ quy để duyệt các đỉnh kề chưa được duyệt.

    def traverse_graph(self, start_vertex, method): # Định nghĩa hàm để thực hiện duyệt đồ thị.
        if method == "BFS": # Kiểm tra xem phương pháp duyệt có là "BFS" (duyệt theo chiều rộng) hay không.
            self.breadth_first_search(start_vertex)  # Duyệt đồ thị theo chiều rộng
        elif method == "DFS": # Kiểm tra xem phương pháp duyệt có là "DFS" (duyệt theo chiều sâu) hay không.
            self.depth_first_search(start_vertex)  # Duyệt đồ thị theo chiều sâu
        else:
            print("Phương pháp duyệt không hợp lệ.")

# Nhập số đỉnh và số cạnh của đồ thị từ bàn phím
num_vertices = int(input("Nhập số đỉnh của đồ thị: "))
num_edges = int(input("Nhập số cạnh của đồ thị: "))

# Tạo đối tượng đồ thị
graph = Graph()

# Thêm các đỉnh vào đồ thị
for i in range(num_vertices):
    value = input(f"Nhập đỉnh thứ {i+1}: ")
    graph.add_vertex(value)

# Thêm các cạnh vào đồ thị
for i in range(num_edges):
    edge = input(f"Nhập cạnh thứ {i+1}: ")
    source, destination = edge.split()
    graph.add_edge(source, destination)

# Duyệt đồ thị
start_vertex = input("Nhập đỉnh bắt đầu (BFS/DFS): ")
method = input("Chọn phương pháp duyệt (BFS/DFS): ")
graph.traverse_graph(graph.vertices[start_vertex], method)

# In đồ thị
print("Đồ thị:")
graph.print_graph()


