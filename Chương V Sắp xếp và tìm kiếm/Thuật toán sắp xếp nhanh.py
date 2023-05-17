def heapify(arr, n, i, is_max_heap):
    """
    Tạo một heap từ một mảng
    """
    if is_max_heap:
        largest = i  # lưu chỉ số phần tử lớn nhất
        left = 2 * i + 1  # lưu chỉ số phần tử con bên trái
        right = 2 * i + 2  # lưu chỉ số phần tử con bên phải
 
        # So sánh phần tử lớn nhất với phần tử con bên trái
        if left < n and arr[i] < arr[left]:
            largest = left
 
        # So sánh phần tử lớn nhất với phần tử con bên phải
        if right < n and arr[largest] < arr[right]:
            largest = right
 
        # Nếu phần tử lớn nhất không phải là phần tử cha thì hoán đổi và tái tạo heap
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # hoán đổi
            heapify(arr, n, largest, is_max_heap)
    else:
        smallest = i  # lưu chỉ số phần tử nhỏ nhất
        left = 2 * i + 1  # lưu chỉ số phần tử con bên trái
        right = 2 * i + 2  # lưu chỉ số phần tử con bên phải
 
        # So sánh phần tử nhỏ nhất với phần tử con bên trái
        if left < n and arr[i] > arr[left]:
            smallest = left
 
        # So sánh phần tử nhỏ nhất với phần tử con bên phải
        if right < n and arr[smallest] > arr[right]:
            smallest = right
 
        # Nếu phần tử nhỏ nhất không phải là phần tử cha thì hoán đổi và tái tạo heap
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]  # hoán đổi
            heapify(arr, n, smallest, is_max_heap)
 
 
def heap_sort(arr, is_max_heap=True):
    """
    Sắp xếp một mảng bằng thuật toán heap sort
    """
    n = len(arr)
 
    # Xây dựng heap từ mảng
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, is_max_heap)
 
    # Lấy phần tử đầu tiên của heap và đưa vào danh sách kết quả sắp xếp
    result = []
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # hoán đổi
        result.append(arr[i])
        heapify(arr, i, 0, is_max_heap)
    result.append(arr[0])
    result.reverse()
    return result

# Nhập dữ liệu từ bàn
arr = input("Nhập mảng số nguyên cách nhau bởi dấu cách: ").split()
arr = [int(x) for x in arr]
 
is_max_heap = input("Bạn muốn sắp xếp tăng dần hay giảm dần? (true/false): ")
is_max_heap = True if is_max_heap.lower() == "true" else False
 
print("Mảng ban đầu:", arr)
 
sorted_arr = heap_sort(arr, is_max_heap)
print("Mảng đã sắp xếp:", sorted_arr)
