from modules.file_handler import read_csv, write_csv, add_record, get_next_id, ensure_file_exists
from modules.validators import validate_price, validate_id, validate_name

PRODUCTS_FILE = 'data/products.csv'
FIELDNAMES = ['product_id', 'product_name', 'price']

ensure_file_exists(PRODUCTS_FILE)

def add_product(product_name, price):
    if not validate_name(product_name):
        return False, "Invalid product name"
    if not validate_price(price):
        return False, "Invalid price"
    
    product_id = get_next_id(PRODUCTS_FILE, 'product_id')
    record = {
        'product_id': product_id,
        'product_name': product_name,
        'price': str(price)
    }
    
    if add_record(PRODUCTS_FILE, record, FIELDNAMES):
        return True, f"Product added with ID: {product_id}"
    return False, "Failed to add product"

def view_all_products():
    products = read_csv(PRODUCTS_FILE)
    if not products:
        print("No products found")
        return
    
    print("\n" + "="*60)
    print(f"{'ID':<10} {'Product Name':<25} {'Price':<15}")
    print("="*60)
    
    for product in products:
        print(f"{product['product_id']:<10} {product['product_name']:<25} {product['price']:<15}")
    print("="*60)

def search_product(product_id):
    if not validate_id(product_id):
        return None, "Invalid product ID"
    
    products = read_csv(PRODUCTS_FILE)
    for product in products:
        if product['product_id'] == str(product_id):
            return product, ""
    
    return None, "Product not found"

def update_product(product_id, product_name=None, price=None):
    if not validate_id(product_id):
        return False, "Invalid product ID"
    
    products = read_csv(PRODUCTS_FILE)
    found = False
    
    for product in products:
        if product['product_id'] == str(product_id):
            found = True
            if product_name and validate_name(product_name):
                product['product_name'] = product_name
            if price and validate_price(price):
                product['price'] = str(price)
            break
    
    if not found:
        return False, "Product not found"
    
    if write_csv(PRODUCTS_FILE, products, FIELDNAMES):
        return True, "Product updated"
    return False, "Failed to update product"

def delete_product(product_id):
    if not validate_id(product_id):
        return False, "Invalid product ID"
    
    products = read_csv(PRODUCTS_FILE)
    initial_count = len(products)
    products = [p for p in products if p['product_id'] != str(product_id)]
    
    if len(products) == initial_count:
        return False, "Product not found"
    
    if write_csv(PRODUCTS_FILE, products, FIELDNAMES):
        return True, "Product deleted"
    return False, "Failed to delete product"
