from modules.file_handler import read_csv, write_csv, add_record, get_next_id, ensure_file_exists
from modules.validators import validate_name, validate_phone, validate_id

CUSTOMERS_FILE = 'data/customers.csv'
FIELDNAMES = ['customer_id', 'name', 'phone', 'address']

ensure_file_exists(CUSTOMERS_FILE)

def add_customer(name, phone, address):
    if not validate_name(name):
        return False, "Invalid name"
    if not validate_phone(phone):
        return False, "Invalid phone number"
    if not address or len(address) < 2:
        return False, "Invalid address"
    
    customer_id = get_next_id(CUSTOMERS_FILE, 'customer_id')
    record = {
        'customer_id': customer_id,
        'name': name,
        'phone': phone,
        'address': address
    }
    
    if add_record(CUSTOMERS_FILE, record, FIELDNAMES):
        return True, f"Customer added with ID: {customer_id}"
    return False, "Failed to add customer"

def view_all_customers():
    customers = read_csv(CUSTOMERS_FILE)
    if not customers:
        print("No customers found")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Address':<30}")
    print("="*80)
    
    for customer in customers:
        print(f"{customer['customer_id']:<5} {customer['name']:<20} {customer['phone']:<15} {customer['address']:<30}")
    print("="*80)

def search_customer(customer_id):
    if not validate_id(customer_id):
        return None, "Invalid customer ID"
    
    customers = read_csv(CUSTOMERS_FILE)
    for customer in customers:
        if customer['customer_id'] == str(customer_id):
            return customer, ""
    
    return None, "Customer not found"

def update_customer(customer_id, name=None, phone=None, address=None):
    if not validate_id(customer_id):
        return False, "Invalid customer ID"
    
    customers = read_csv(CUSTOMERS_FILE)
    found = False
    
    for customer in customers:
        if customer['customer_id'] == str(customer_id):
            found = True
            if name and validate_name(name):
                customer['name'] = name
            if phone and validate_phone(phone):
                customer['phone'] = phone
            if address and len(address) >= 2:
                customer['address'] = address
            break
    
    if not found:
        return False, "Customer not found"
    
    if write_csv(CUSTOMERS_FILE, customers, FIELDNAMES):
        return True, "Customer updated"
    return False, "Failed to update customer"

def delete_customer(customer_id):
    if not validate_id(customer_id):
        return False, "Invalid customer ID"
    
    customers = read_csv(CUSTOMERS_FILE)
    initial_count = len(customers)
    customers = [c for c in customers if c['customer_id'] != str(customer_id)]
    
    if len(customers) == initial_count:
        return False, "Customer not found"
    
    if write_csv(CUSTOMERS_FILE, customers, FIELDNAMES):
        return True, "Customer deleted"
    return False, "Failed to delete customer"
