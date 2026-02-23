from product_manager import *

products = load_data()

while True:
    print("\n========== MENU ==========")
    print("1. Thêm sản phẩm")
    print("2. Sửa sản phẩm")
    print("3. Xóa sản phẩm")
    print("4. Tìm kiếm sản phẩm")
    print("5. Hiển thị tất cả")
    print("0. Thoát")
    print("==========================")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        products = add_product(products)

    elif choice == "2":
        update_product(products)

    elif choice == "3":
        delete_product(products)

    elif choice == "4":
        search_product_by_name(products)

    elif choice == "5":
        display_all_products(products)

    elif choice == "0":
        save_data(products)
        print("Đã lưu dữ liệu. Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ!")