import os
import csv

# Constants
DATA_FOLDER = "data"
CUSTOMERS_FILE = os.path.join(DATA_FOLDER, "customers.csv")
PRODUCTS_FILE = os.path.join(DATA_FOLDER, "products.csv")
INSTALLMENTS_FILE = os.path.join(DATA_FOLDER, "installments.csv")

# Initialize data folder and CSV files
def initialize_system():
    """Create data folder and CSV files if they don't exist"""
    
    # Create data folder if not exists
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    
    # Create customers.csv if not exists
    if not os.path.exists(CUSTOMERS_FILE):
        with open(CUSTOMERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['customer_id', 'name', 'phone', 'address'])
    
    # Create products.csv if not exists
    if not os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['product_id', 'product_name', 'price'])
    
    # Create installments.csv if not exists
    if not os.path.exists(INSTALLMENTS_FILE):
        with open(INSTALLMENTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['installment_id', 'customer_id', 'product_id', 'total_price', 'paid_amount', 'remaining_amount'])

# Read all data from CSV
def read_csv(filepath):
    """Read and return all rows from a CSV file"""
    rows = []
    try:
        with open(filepath, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)
            for row in reader:
                rows.append(row)
    except Exception as e:
        print(f"Error reading file: {e}")
    return rows

# Write data to CSV
def write_csv(filepath, rows):
    """Write rows to a CSV file"""
    try:
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except Exception as e:
        print(f"Error writing file: {e}")

# Check if ID exists in CSV
def id_exists(filepath, column_index, id_value):
    """Check if an ID exists in the specified column"""
    rows = read_csv(filepath)
    for i in range(1, len(rows)):  # Skip header
        if rows[i][column_index] == id_value:
            return True
    return False

# Get next ID (auto-increment)
def get_next_id(filepath, column_index):
    """Get the next available ID"""
    rows = read_csv(filepath)
    if len(rows) <= 1:  # Only header
        return 1
    max_id = 0
    for i in range(1, len(rows)):
        try:
            id_val = int(rows[i][column_index])
            if id_val > max_id:
                max_id = id_val
        except:
            pass
    return max_id + 1

# Customer Management Functions
def add_customer():
    """Add a new customer"""
    try:
        print("\n--- Add Customer ---")
        
        # Get customer input
        customer_id_input = input("Enter customer ID (numeric): ").strip()
        
        # Validate numeric ID
        try:
            customer_id = int(customer_id_input)
        except ValueError:
            print("Error: Customer ID must be numeric!")
            return
        
        # Check if ID already exists
        if id_exists(CUSTOMERS_FILE, 0, str(customer_id)):
            print(f"Error: Customer ID {customer_id} already exists!")
            return
        
        name = input("Enter customer name: ").strip()
        if not name:
            print("Error: Name cannot be empty!")
            return
        
        phone = input("Enter phone number: ").strip()
        if not phone:
            print("Error: Phone cannot be empty!")
            return
        
        address = input("Enter address: ").strip()
        if not address:
            print("Error: Address cannot be empty!")
            return
        
        # Write to CSV
        rows = read_csv(CUSTOMERS_FILE)
        rows.append([str(customer_id), name, phone, address])
        write_csv(CUSTOMERS_FILE, rows)
        
        print(f"Success: Customer {name} added with ID {customer_id}!")
        
    except Exception as e:
        print(f"Error: {e}")

def view_customers():
    """View all customers"""
    try:
        print("\n--- Customers ---")
        rows = read_csv(CUSTOMERS_FILE)
        
        if len(rows) <= 1:
            print("No customers found.")
            return
        
        # Print header
        print(f"{rows[0][0]:<12} | {rows[0][1]:<20} | {rows[0][2]:<15} | {rows[0][3]:<20}")
        print("-" * 75)
        
        # Print data
        for i in range(1, len(rows)):
            print(f"{rows[i][0]:<12} | {rows[i][1]:<20} | {rows[i][2]:<15} | {rows[i][3]:<20}")
            
    except Exception as e:
        print(f"Error: {e}")

# Product Management Functions
def add_product():
    """Add a new product"""
    try:
        print("\n--- Add Product ---")
        
        # Get product input
        product_id_input = input("Enter product ID (numeric): ").strip()
        
        # Validate numeric ID
        try:
            product_id = int(product_id_input)
        except ValueError:
            print("Error: Product ID must be numeric!")
            return
        
        # Check if ID already exists
        if id_exists(PRODUCTS_FILE, 0, str(product_id)):
            print(f"Error: Product ID {product_id} already exists!")
            return
        
        product_name = input("Enter product name: ").strip()
        if not product_name:
            print("Error: Product name cannot be empty!")
            return
        
        price_input = input("Enter price (numeric): ").strip()
        
        # Validate numeric price
        try:
            price = float(price_input)
            if price < 0:
                print("Error: Price cannot be negative!")
                return
        except ValueError:
            print("Error: Price must be numeric!")
            return
        
        # Write to CSV
        rows = read_csv(PRODUCTS_FILE)
        rows.append([str(product_id), product_name, str(price)])
        write_csv(PRODUCTS_FILE, rows)
        
        print(f"Success: Product {product_name} added with ID {product_id} at price {price}!")
        
    except Exception as e:
        print(f"Error: {e}")

def view_products():
    """View all products"""
    try:
        print("\n--- Products ---")
        rows = read_csv(PRODUCTS_FILE)
        
        if len(rows) <= 1:
            print("No products found.")
            return
        
        # Print header
        print(f"{rows[0][0]:<12} | {rows[0][1]:<20} | {rows[0][2]:<12}")
        print("-" * 50)
        
        # Print data
        for i in range(1, len(rows)):
            print(f"{rows[i][0]:<12} | {rows[i][1]:<20} | {rows[i][2]:<12}")
            
    except Exception as e:
        print(f"Error: {e}")

# Installment Management Functions
def create_installment():
    """Create a new installment"""
    try:
        print("\n--- Create Installment ---")
        
        # Get customer ID
        customer_id_input = input("Enter customer ID: ").strip()
        
        # Check if customer exists
        if not id_exists(CUSTOMERS_FILE, 0, customer_id_input):
            print(f"Error: Customer ID {customer_id_input} not found!")
            return
        
        # Get product ID
        product_id_input = input("Enter product ID: ").strip()
        
        # Check if product exists
        if not id_exists(PRODUCTS_FILE, 0, product_id_input):
            print(f"Error: Product ID {product_id_input} not found!")
            return
        
        # Get total price
        total_price_input = input("Enter total price (numeric): ").strip()
        
        try:
            total_price = float(total_price_input)
            if total_price < 0:
                print("Error: Total price cannot be negative!")
                return
        except ValueError:
            print("Error: Total price must be numeric!")
            return
        
        # Get paid amount
        paid_amount_input = input("Enter paid amount (numeric): ").strip()
        
        try:
            paid_amount = float(paid_amount_input)
            if paid_amount < 0:
                print("Error: Paid amount cannot be negative!")
                return
            if paid_amount > total_price:
                print("Error: Paid amount cannot exceed total price!")
                return
        except ValueError:
            print("Error: Paid amount must be numeric!")
            return
        
        # Calculate remaining amount
        remaining_amount = total_price - paid_amount
        
        # Generate installment ID
        installment_id = get_next_id(INSTALLMENTS_FILE, 0)
        
        # Write to CSV
        rows = read_csv(INSTALLMENTS_FILE)
        rows.append([str(installment_id), customer_id_input, product_id_input, str(total_price), str(paid_amount), str(remaining_amount)])
        write_csv(INSTALLMENTS_FILE, rows)
        
        print(f"Success: Installment {installment_id} created!")
        print(f"Total Price: {total_price}, Paid: {paid_amount}, Remaining: {remaining_amount}")
        
    except Exception as e:
        print(f"Error: {e}")

def pay_installment():
    """Update payment for an installment"""
    try:
        print("\n--- Pay Installment ---")
        
        # Get installment ID
        installment_id_input = input("Enter installment ID: ").strip()
        
        # Find installment
        rows = read_csv(INSTALLMENTS_FILE)
        installment_index = -1
        
        for i in range(1, len(rows)):
            if rows[i][0] == installment_id_input:
                installment_index = i
                break
        
        if installment_index == -1:
            print(f"Error: Installment ID {installment_id_input} not found!")
            return
        
        # Get current values
        current_paid = float(rows[installment_index][4])
        current_remaining = float(rows[installment_index][5])
        total_price = float(rows[installment_index][3])
        
        # Get payment amount
        payment_input = input(f"Enter payment amount (remaining: {current_remaining}): ").strip()
        
        try:
            payment = float(payment_input)
            if payment < 0:
                print("Error: Payment amount cannot be negative!")
                return
            if payment > current_remaining:
                print(f"Error: Payment cannot exceed remaining amount ({current_remaining})!")
                return
        except ValueError:
            print("Error: Payment amount must be numeric!")
            return
        
        # Update amounts
        new_paid = current_paid + payment
        new_remaining = current_remaining - payment
        
        # Update CSV
        rows[installment_index][4] = str(new_paid)
        rows[installment_index][5] = str(new_remaining)
        write_csv(INSTALLMENTS_FILE, rows)
        
        print(f"Success: Payment {payment} recorded!")
        print(f"New Paid: {new_paid}, Remaining: {new_remaining}")
        
    except Exception as e:
        print(f"Error: {e}")

def view_installments():
    """View all installments"""
    try:
        print("\n--- Installments ---")
        rows = read_csv(INSTALLMENTS_FILE)
        
        if len(rows) <= 1:
            print("No installments found.")
            return
        
        # Print header
        print(f"{'ID':<6} | {'Cust':<8} | {'Prod':<8} | {'Total':<10} | {'Paid':<10} | {'Remaining':<10}")
        print("-" * 70)
        
        # Print data
        for i in range(1, len(rows)):
            print(f"{rows[i][0]:<6} | {rows[i][1]:<8} | {rows[i][2]:<8} | {rows[i][3]:<10} | {rows[i][4]:<10} | {rows[i][5]:<10}")
            
    except Exception as e:
        print(f"Error: {e}")

# Login Menu
def show_login_menu():
    """Display the login menu"""
    print("\n" + "="*50)
    print("INSTALLMENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    print("="*50)

# Admin Menu
def show_admin_menu():
    """Display the admin menu"""
    print("\n" + "="*50)
    print("ADMIN PANEL")
    print("="*50)
    print("1. Add Customer")
    print("2. Add Product")
    print("3. Create Installment")
    print("4. Pay Installment")
    print("5. View Customers")
    print("6. View Products")
    print("7. View Installments")
    print("8. Back to Main Menu")
    print("="*50)

# User Menu
def user_panel():
    """User view their own installments"""
    try:
        customer_id = input("\nEnter your Customer ID: ").strip()
        
        # Check if customer exists
        if not id_exists(CUSTOMERS_FILE, 0, customer_id):
            print(f"Error: Customer ID {customer_id} not found!")
            return
        
        # Get customer details
        rows = read_csv(CUSTOMERS_FILE)
        customer_data = None
        for i in range(1, len(rows)):
            if rows[i][0] == customer_id:
                customer_data = rows[i]
                break
        
        print("\n--- Your Details ---")
        print(f"Customer ID: {customer_data[0]}")
        print(f"Name: {customer_data[1]}")
        print(f"Phone: {customer_data[2]}")
        print(f"Address: {customer_data[3]}")
        
        # View customer's installments
        print("\n--- Your Installments ---")
        installment_rows = read_csv(INSTALLMENTS_FILE)
        
        if len(installment_rows) <= 1:
            print("No installments found.")
            return
        
        print(f"{'ID':<6} | {'Product ID':<12} | {'Total':<10} | {'Paid':<10} | {'Remaining':<10}")
        print("-" * 65)
        
        found = False
        for i in range(1, len(installment_rows)):
            if installment_rows[i][1] == customer_id:
                found = True
                print(f"{installment_rows[i][0]:<6} | {installment_rows[i][2]:<12} | {installment_rows[i][3]:<10} | {installment_rows[i][4]:<10} | {installment_rows[i][5]:<10}")
        
        if not found:
            print("No installments found for your account.")
            
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main program loop"""
    initialize_system()
    
    while True:
        show_login_menu()
        
        try:
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                # Admin Panel
                admin_panel()
            elif choice == '2':
                # User Panel
                user_panel()
            elif choice == '3':
                print("\nThank you for using Installment Management System!")
                break
            else:
                print("Error: Invalid choice! Please enter 1-3.")
                
        except Exception as e:
            print(f"Error: {e}")

def admin_panel():
    """Admin control panel with all features"""
    while True:
        show_admin_menu()
        
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                add_customer()
            elif choice == '2':
                add_product()
            elif choice == '3':
                create_installment()
            elif choice == '4':
                pay_installment()
            elif choice == '5':
                view_customers()
            elif choice == '6':
                view_products()
            elif choice == '7':
                view_installments()
            elif choice == '8':
                print("\nReturning to main menu...\n")
                break
            else:
                print("Error: Invalid choice! Please enter 1-8.")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
