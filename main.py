import modules.customer as customer
import modules.product as product
import modules.installment as installment

def print_start_menu():
    print("\n" + "="*60)
    print("  INSTALLMENT MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Admin Panel (Full Control)")
    print("2. Customer Panel (View Only)")
    print("3. Exit")
    print("-"*60)

def print_admin_menu():
    print("\n" + "="*60)
    print("      ADMIN PANEL")
    print("="*60)
    print("1. Customer Management")
    print("2. Product Management")
    print("3. Installment Management")
    print("4. Back to Start")
    print("-"*60)

def print_customer_view_menu():
    print("\n" + "="*60)
    print("      CUSTOMER PANEL (View Only)")
    print("="*60)
    print("1. View All Customers")
    print("2. View All Products")
    print("3. View All Installments")
    print("4. Back to Start")
    print("-"*60)

def customer_menu():
    while True:
        print("\n" + "="*60)
        print("      CUSTOMER MANAGEMENT")
        print("="*60)
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Add Customer ---")
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            address = input("Enter address: ").strip()
            
            success, message = customer.add_customer(name, phone, address)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '2':
            print("\n--- All Customers ---")
            customer.view_all_customers()
        
        elif choice == '3':
            print("\n--- Search Customer ---")
            customer_id = input("Enter customer ID: ").strip()
            cust, message = customer.search_customer(customer_id)
            
            if cust:
                print(f"\nID: {cust['customer_id']}")
                print(f"Name: {cust['name']}")
                print(f"Phone: {cust['phone']}")
                print(f"Address: {cust['address']}")
            else:
                print(f"✗ {message}")
        
        elif choice == '4':
            print("\n--- Update Customer ---")
            customer_id = input("Enter customer ID: ").strip()
            name = input("Enter new name (blank to skip): ").strip() or None
            phone = input("Enter new phone (blank to skip): ").strip() or None
            address = input("Enter new address (blank to skip): ").strip() or None
            
            success, message = customer.update_customer(customer_id, name, phone, address)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '5':
            print("\n--- Delete Customer ---")
            customer_id = input("Enter customer ID: ").strip()
            confirm = input("Confirm (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                success, message = customer.delete_customer(customer_id)
                print(f"✓ {message}" if success else f"✗ {message}")
            else:
                print("✗ Cancelled")
        
        elif choice == '6':
            break
        else:
            print("✗ Invalid choice")

def product_menu():
    while True:
        print("\n" + "="*60)
        print("      PRODUCT MANAGEMENT")
        print("="*60)
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Add Product ---")
            product_name = input("Enter product name: ").strip()
            price = input("Enter price: ").strip()
            
            success, message = product.add_product(product_name, price)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '2':
            print("\n--- All Products ---")
            product.view_all_products()
        
        elif choice == '3':
            print("\n--- Search Product ---")
            product_id = input("Enter product ID: ").strip()
            prod, message = product.search_product(product_id)
            
            if prod:
                print(f"\nID: {prod['product_id']}")
                print(f"Name: {prod['product_name']}")
                print(f"Price: {prod['price']}")
            else:
                print(f"✗ {message}")
        
        elif choice == '4':
            print("\n--- Update Product ---")
            product_id = input("Enter product ID: ").strip()
            product_name = input("Enter new name (blank to skip): ").strip() or None
            price = input("Enter new price (blank to skip): ").strip() or None
            
            success, message = product.update_product(product_id, product_name, price)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '5':
            print("\n--- Delete Product ---")
            product_id = input("Enter product ID: ").strip()
            confirm = input("Confirm (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                success, message = product.delete_product(product_id)
                print(f"✓ {message}" if success else f"✗ {message}")
            else:
                print("✗ Cancelled")
        
        elif choice == '6':
            break
        else:
            print("✗ Invalid choice")

def installment_menu():
    while True:
        print("\n" + "="*60)
        print("      INSTALLMENT MANAGEMENT")
        print("="*60)
        print("1. Create Installment")
        print("2. View All Installments")
        print("3. Search Installment")
        print("4. Make Payment")
        print("5. Customer Total Balance")
        print("6. Customer Installments")
        print("7. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter choice (1-7): ").strip()
        
        if choice == '1':
            print("\n--- Create Installment ---")
            customer_id = input("Enter customer ID: ").strip()
            product_id = input("Enter product ID: ").strip()
            paid_amount = input("Enter paid amount: ").strip()
            
            success, message = installment.create_installment(customer_id, product_id, paid_amount)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '2':
            print("\n--- All Installments ---")
            installment.view_all_installments()
        
        elif choice == '3':
            print("\n--- Search Installment ---")
            installment_id = input("Enter installment ID: ").strip()
            inst, message = installment.search_installment(installment_id)
            
            if inst:
                print(f"\nInstallment ID: {inst['installment_id']}")
                print(f"Customer ID: {inst['customer_id']}")
                print(f"Product ID: {inst['product_id']}")
                print(f"Total Price: {inst['total_price']}")
                print(f"Paid Amount: {inst['paid_amount']}")
                print(f"Remaining: {inst['remaining_amount']}")
                remaining = float(inst['remaining_amount'])
                status = "FULLY PAID" if remaining == 0 else "PENDING"
                print(f"Status: {status}")
            else:
                print(f"✗ {message}")
        
        elif choice == '4':
            print("\n--- Make Payment ---")
            installment_id = input("Enter installment ID: ").strip()
            payment_amount = input("Enter payment amount: ").strip()
            
            success, message = installment.make_payment(installment_id, payment_amount)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '5':
            print("\n--- Customer Total Balance ---")
            customer_id = input("Enter customer ID: ").strip()
            balance, message = installment.get_customer_total_balance(customer_id)
            
            if message == "":
                print(f"✓ Total Balance: {balance}")
            else:
                print(f"✗ {message}")
        
        elif choice == '6':
            print("\n--- Customer Installments ---")
            customer_id = input("Enter customer ID: ").strip()
            installations, message = installment.get_customer_installments(customer_id)
            
            if installations:
                print(f"{'ID':<5} {'Product':<5} {'Total':<12} {'Paid':<12} {'Remaining':<12} {'Status':<15}")
                print("-"*60)
                
                for inst in installations:
                    remaining = float(inst['remaining_amount'])
                    status = "FULLY PAID" if remaining == 0 else "PENDING"
                    
                    print(f"{inst['installment_id']:<5} {inst['product_id']:<5} {inst['total_price']:<12} "
                          f"{inst['paid_amount']:<12} {inst['remaining_amount']:<12} {status:<15}")
            else:
                print(f"✗ {message}")
        
        elif choice == '7':
            break
        else:
            print("✗ Invalid choice")

def main():
    while True:
        print_start_menu()
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            admin_panel()
        elif choice == '2':
            customer_panel()
        elif choice == '3':
            print("\n" + "="*60)
            print("Thank you for using Installment Management System!")
            print("="*60 + "\n")
            break
        else:
            print("✗ Invalid choice")

def admin_panel():
    while True:
        print_admin_menu()
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            customer_menu()
        elif choice == '2':
            product_menu()
        elif choice == '3':
            installment_menu()
        elif choice == '4':
            break
        else:
            print("✗ Invalid choice")

def customer_panel():
    while True:
        print_customer_view_menu()
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            print("\n--- All Customers ---")
            customer.view_all_customers()
        
        elif choice == '2':
            print("\n--- All Products ---")
            product.view_all_products()
        
        elif choice == '3':
            print("\n--- All Installments ---")
            installment.view_all_installments()
        
        elif choice == '4':
            break
        
        else:
            print("✗ Invalid choice")

if __name__ == "__main__":
    main()
