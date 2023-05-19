def bubble_sort(arr, ascending):
    n = len(arr) # Lấy độ dài của danh sách
    step = 0 # Đếm số bươc sắp xếp
    # Duyệt qua từng phần tử của mảng
    for i in range(n):
        # Duyệt qua từng phần tử của mảng trừ i (các phần tử đã được sắp xếp)
        for j in range(n - i - 1):
            # So sánh hai phần tử liên tiếp và đổi chỗ nếu chúng không ở đúng vị trí
            if ascending and arr[j] > arr[j + 1] or not ascending and arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # In ra trình tự các bước sắp xếp
            step += 1
            print(f"Bước {step}: {arr}")
    return arr

# Nhập dữ liệu từ bàn phím
arr = []
n = int(input("Nhập số phần tử của mảng: "))
for i in range(n):
    arr.append(int(input("Nhập phần tử thứ %d: " % (i + 1))))

# Lựa chọn sắp xếp tăng dần hoặc giảm dần
ascending = input("Sắp xếp tăng dần? (Y/N): ")
if ascending.lower() == 'y':
    ascending = True
else:
    ascending = False

# Sử dụng hàm để sắp xếp mảng và in trình tự các bước sắp xếp
print("Trình tự các bước sắp xếp:")
bubble_sort(arr, ascending)

# In kết quả sắp xếp
if ascending:
    print("Mảng đã sắp xếp tăng dần:")
else:
    print("Mảng đã sắp xếp giảm dần:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
