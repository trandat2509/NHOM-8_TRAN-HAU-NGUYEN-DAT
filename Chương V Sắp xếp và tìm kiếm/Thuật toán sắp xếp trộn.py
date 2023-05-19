def merge_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    
    # Chia danh sách thành hai nửa
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Sắp xếp các nửa danh sách
    left_half = merge_sort(left_half, ascending)
    right_half = merge_sort(right_half, ascending)
    
    # Trộn các nửa danh sách đã sắp xếp lại với nhau
    sorted_arr = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if (ascending and left_half[i] <= right_half[j]) or (not ascending and left_half[i] >= right_half[j]):
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    sorted_arr += left_half[i:]
    sorted_arr += right_half[j:]
    
    # In các bước sắp xếp ra màn hình
    print(f"Tách {arr} thành {left_half} và {right_half}")
    print(f"Sắp xếp {left_half} và {right_half} thành {sorted_arr}")
    
    return sorted_arr

# Nhập dữ liệu từ bàn phím
arr = list(map(int, input("Nhập danh sách các số cách nhau bởi dấu cách: ").split()))
ascending = input("Sắp xếp tăng dần (y/n)? ").lower() == "y"

# Sắp xếp danh sách
sorted_arr = merge_sort(arr, ascending)

# In kết quả đã sắp xếp
print("Danh sách đã sắp xếp:", sorted_arr)
