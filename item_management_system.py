items = [
    {"ID":"SP001","name":"Chuột không dây Logitech","price":"250000","stock":"15","safety_stock":"20","total_price":"3750000","status":"Cảnh báo"},
    {"ID":"SP002","name":"Laptop MSI","price":"23000000","stock":"22","safety_stock":"20","total_price":"3750000","status":"Còn hàng"},
    {"ID":"SP003","name":"Bàn Phím Katana","price":"2100000","stock":"19","safety_stock":"20","total_price":"3750000","status":"Cảnh báo"},
    {"ID":"SP004","name":"Đồng hồ Apple Watch","price":"5200000","stock":"30","safety_stock":"20","total_price":"3750000","status":"Còn hàng"},
    {"ID":"SP005","name":"Tai nghe Airpods","price":"1800000","stock":"34","safety_stock":"20","total_price":"3750000","status":"Còn hàng"}
]
'''
def auto_calculate(price,stock):
    total_price = price * stock
    if total_price = 0: 
        status= "Hết hàng"
    elif total_price < safety_stock:
        status= "Cảnh báo ( Cần nhập hàng )"
    elif safety_stock <= total_price <= 3*safety_stock:
        status= "An toàn"
    elif total_price > 3*safety_stock:
        status= "Quá tải ( Thặng dư )"
    return total_price,status
'''

def display_menu():
    option = [
        "Hiển thị danh sách kho hàng",
        "Khai báo sản phẩm mới",
        "Cập nhật số lượng và giá vốn",
        "Xóa sản phẩm khỏi danh mục",
        "Tìm kiếm sản phẩm",
        "Thống kê trạng thái kho hàng",
        "Phân loại trạng thái tự động",
        "Thoát chương trình"
    ]
    print("="*70)
    print(f"{'ITEM MANAGEMENT SYSTEM':^70}")
    print("="*70)
    for index, option in enumerate ( option, 1):
        print(f"| {index} . {option :<70}|")
    
    print("="*70)


def display_item(items_list= None):
    if items_list is None:
        items_list = items
    if not items_list:
        print("Danh sách sản phẩm đang trống.")
    print("-"*163)
    print(f" {'DANH SÁCH KHO HÀNG HIỆN CÓ':^163} ")
    print("-"*163)
    print(f"| {'Mã sản phẩm':<13} | {'Tên sản phẩm':<30} | {'Đơn giá (VNĐ)':^15} | {'Số lượng tồn kho':^20} | {'Định mức tối thiểu':^20} | {'Tổng giá trị':^15} | {'Trạng thái tồn kho':<28} |")
    for i in items:
        print(f"| {i["ID"]:<13} | {i["name"]:<30} | {i["price"]:^15} | {i["stock"]:^20} | {i["safety_stock"]:^20} | {i["total_price"]:^15} | {i["status"]:<28} | ")
    print("-"*163)


def add_item():
    print("-"*45)
    print(f" {'NHẬP THÔNG TIN SẢN PHẨM MỚI:':^45} ")
    print("-"*45)
    while True:
        input_id = input("Nhập mã sản phẩm: ").strip()
        if not input_id:
            print("ID sản phẩm không được để trống.")
            continue
        is_exist = False
        for i in items:
            if i["ID"].upper() == input_id.upper():
                is_exist = True
                break
        if is_exist:
            print("Mã sản phẩm đã tồn tại, vui lòng nhập lại")
        else:
            input_id=input_id.upper()
            break
        while True:
            input_name = input("Nhập tên sản phẩm :").strip()
            if input_name:
                break
            print("Tên sản phẩm không được để trống")
        while True:
            try:
                input_price = int(input("Nhập giá sản phẩm :"))
                if input_price >= 0:
                    break
                print("Giá sản phẩm không được là số âm")
                
            except ValueError:
                print("Vui lòng nhập số nguyên")
        
        while True:
            try:
                input_stock = int(input("Nhập số lượng sản phẩm :"))
                if input_stock >= 0:
                    break
                print("Số lượng sản phẩm không được là số âm")
                
            except ValueError:
                print("Vui lòng nhập số nguyên")
        
        while True:
            try:
                input_safety_stock= int(input("Nhập định mức tối thiểu :"))
                if input_safety_stock >= 0:
                    break
                print("Định mức tối thiểu không được là số âm")
                
            except ValueError:
                print("Vui lòng nhập số nguyên")
        

def delete_item():
    input_id = input("Nhập mã sản phẩm cần xóa:").strip().upper()
    for i in items:
        if i["ID"] == input_id:
            confirm = input("Bạn có muốn xóa sản phẩm không (Y/N): ").strip().upper()
        if confirm == 'Y':
            items.remove(i)
            print("Đã xóa sản phẩm khỏi hệ thống")
        else:
            print("Đã hủy thao tác xóa")
        return
    print("Không tìm thấy sãn phẩm có mã này")

def search_item():
    keyword = input("Nhập mã sản phẩm hoặc tên sản phẩm cần tìm:").strip().lower()
    found_items = []
    for i in items:
        if keyword == i['ID'].lower() or keyword in i['name'].lower():
            found_items.append(i)
    if found_items:
        print("Tìm thấy sản phẩm")
        display_item(found_items)
    else:
        print("Không tìm thấy sản phẩm nào phù hợp")
    


def main():
    while True:
        display_menu()
        choice = input("Nhập lựa chọn chức năng (1-8): ").strip()
        match choice:
            case '1':
                display_item()
            case '2':
                add_item()
            case '3':
                pass
            case '4':
                delete_item()
            case '5':
                search_item()
            case '6':
                pass
            case '7':
                pass
            case '8':
                print("Cảm ơn đã sử dụng chương trình. Tạm biệt")
                break
            case _:
                print("Vui lòng nhập lựa chọn phù hợp.")
                continue
    

if __name__ == "__main__":
    main()
