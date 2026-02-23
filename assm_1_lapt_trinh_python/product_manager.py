import json


def load_data():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
            return []


def save_data(products):
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)


def add_product(products):
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá tiền: "))
    quantity = int(input("Nhập số lượng: "))

    new_id = "LT" + str(len(products) + 1).zfill(2)

    new_product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }

    products.append(new_product)
    print("Thêm sản phẩm thành công!")
    return products


def update_product(products):
    product_id = input("Nhập ID sản phẩm cần sửa: ")

    for product in products:
        if product["id"] == product_id:
            product["name"] = input("Nhập tên mới: ")
            product["brand"] = input("Nhập thương hiệu mới: ")
            product["price"] = int(input("Nhập giá mới: "))
            product["quantity"] = int(input("Nhập số lượng mới: "))
            print("Cập nhật thành công!")
            return

    print("Không tìm thấy sản phẩm!")


def delete_product(products):
    product_id = input("Nhập ID sản phẩm cần xóa: ")

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Xóa thành công!")
            return

    print("Không tìm thấy sản phẩm!")


def search_product_by_name(products):
    keyword = input("Nhập từ khóa tìm kiếm: ").lower()

    found = False
    for product in products:
        if keyword in product["name"].lower():
            print(product)
            found = True

    if not found:
        print("Không tìm thấy sản phẩm!")


def display_all_products(products):
    if not products:
        print("Kho hàng trống.")
        return

    for product in products:
        print("ID:", product["id"])
        print("Name:", product["name"])
        print("Brand:", product["brand"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])
        print("--------------------------")