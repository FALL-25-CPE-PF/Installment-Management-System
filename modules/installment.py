from modules.file_handler import read_csv, write_csv, add_record, get_next_id, ensure_file_exists
from modules.validators import validate_id, validate_amount
from modules.customer import search_customer
from modules.product import search_product

INSTALLMENTS_FILE = 'data/installments.csv'
FIELDNAMES = ['installment_id', 'customer_id', 'product_id', 'total_price', 'paid_amount', 'remaining_amount']

ensure_file_exists(INSTALLMENTS_FILE)

def create_installment(customer_id, product_id, paid_amount):
    if not validate_id(customer_id):
        return False, "Invalid customer ID"
    if not validate_id(product_id):
        return False, "Invalid product ID"
    
    customer, msg = search_customer(customer_id)
    if not customer:
        return False, "Customer not found"
    
    product, msg = search_product(product_id)
    if not product:
        return False, "Product not found"
    
    total_price = float(product['price'])
    
    if not validate_amount(paid_amount):
        return False, "Invalid paid amount"
    
    paid_amt = float(paid_amount)
    if paid_amt > total_price:
        return False, "Paid amount exceeds total price"
    
    remaining = total_price - paid_amt
    installment_id = get_next_id(INSTALLMENTS_FILE, 'installment_id')
    
    record = {
        'installment_id': installment_id,
        'customer_id': str(customer_id),
        'product_id': str(product_id),
        'total_price': str(total_price),
        'paid_amount': str(paid_amt),
        'remaining_amount': str(remaining)
    }
    
    if add_record(INSTALLMENTS_FILE, record, FIELDNAMES):
        return True, f"Installment created with ID: {installment_id}"
    return False, "Failed to create installment"

def view_all_installments():
    installments = read_csv(INSTALLMENTS_FILE)
    if not installments:
        print("No installments found")
        return
    
    print("\n" + "="*130)
    print(f"{'ID':<5} {'Cust':<5} {'Prod':<5} {'Total':<12} {'Paid':<12} {'Remaining':<12} {'Status':<15} {'Customer':<20}")
    print("="*130)
    
    for inst in installments:
        customer, _ = search_customer(inst['customer_id'])
        remaining = float(inst['remaining_amount'])
        status = "Fully Paid" if remaining == 0 else "Pending"
        customer_name = customer['name'] if customer else "Unknown"
        
        print(f"{inst['installment_id']:<5} {inst['customer_id']:<5} {inst['product_id']:<5} "
              f"{inst['total_price']:<12} {inst['paid_amount']:<12} {inst['remaining_amount']:<12} "
              f"{status:<15} {customer_name:<20}")
    print("="*130)

def search_installment(installment_id):
    try:
        inst_id = int(installment_id)
        if inst_id <= 0:
            return None, "Invalid installment ID"
    except:
        return None, "Invalid installment ID"
    
    installments = read_csv(INSTALLMENTS_FILE)
    for inst in installments:
        if inst['installment_id'] == str(installment_id):
            return inst, ""
    
    return None, "Installment not found"

def make_payment(installment_id, payment_amount):
    if not validate_amount(payment_amount):
        return False, "Invalid payment amount"
    
    installment, msg = search_installment(installment_id)
    if not installment:
        return False, msg
    
    current_remaining = float(installment['remaining_amount'])
    payment_amt = float(payment_amount)
    
    if payment_amt > current_remaining:
        return False, f"Payment exceeds remaining balance ({current_remaining})"
    
    new_paid = float(installment['paid_amount']) + payment_amt
    new_remaining = current_remaining - payment_amt
    
    installments = read_csv(INSTALLMENTS_FILE)
    for inst in installments:
        if inst['installment_id'] == str(installment_id):
            inst['paid_amount'] = str(new_paid)
            inst['remaining_amount'] = str(new_remaining)
            break
    
    if write_csv(INSTALLMENTS_FILE, installments, FIELDNAMES):
        status = "FULLY PAID" if new_remaining == 0 else f"Remaining: {new_remaining}"
        return True, f"Payment successful. {status}"
    return False, "Failed to process payment"

def get_customer_installments(customer_id):
    if not validate_id(customer_id):
        return [], "Invalid customer ID"
    
    customer, msg = search_customer(customer_id)
    if not customer:
        return [], "Customer not found"
    
    installments = read_csv(INSTALLMENTS_FILE)
    customer_installments = [i for i in installments if i['customer_id'] == str(customer_id)]
    
    return customer_installments, ""

def get_customer_total_balance(customer_id):
    installments, msg = get_customer_installments(customer_id)
    
    if not installments:
        return 0, "No installments found for this customer"
    
    total_balance = sum(float(i['remaining_amount']) for i in installments)
    return total_balance, ""
