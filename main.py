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

