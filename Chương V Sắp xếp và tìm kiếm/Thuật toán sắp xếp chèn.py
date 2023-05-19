def insertion_sort(arr, ascending):
    n = len(arr) # Lấy độ dài của danh sách
    for i in range(1, n): # Duyệt qua tưng từng phần tử trong danh sách, bắt đầu từ phần tử thứ 2
        key = arr[i] # Lưu giá trị hiện tại của phần tử vào biến key
        j = i - 1 # Khởi tạo biến j với giá trị là chỉ số của phàn tử liền trước với phần tử hiện tại
        # Duyệt ngược lại phần tử liên trước phần tử hiện tại đến phân tử đầu danh sách
        while j >= 0 and (arr[j] > key if ascending else arr[j] < key): 
            arr[j + 1] = arr[j] 
            j -= 1 
        arr[j + 1] = key
        print(f"Bước {i}: {arr}") # in ra bước trung gian
    return arr # Trả về danh sách đã sắp xếp

if __name__ == "__main__":
    data = input("Nhập dữ liệu (các số nguyên, cách nhau bởi dấu cách): ")
    order = input("Sắp xếp theo thứ tự ascending (tăng dần) / descending (giảm dần): ")

    data = data.split() # Chuyển chuỗi thành danh sách các chuỗi con
    data = [int(x) for x in data] # Chuyển danh sách các chuỗi thành danh sách các số nguyên

    if order.lower() == "ascending":
        print("Sắp xếp theo tăng dần")
        sorted_data = insertion_sort(data, True)

    elif order.lower() == "descending":
        print("Sắp xếp theo giảm dần")
        sorted_data = insertion_sort(data, False)
    else:
        print("Thứ tự sắp xếp không hợp lệ")
        sorted_data = []

    if sorted_data:
        print("Dữ liệu đã sắp xếp: ", sorted_data)
