def validate_phone(phone):
    if not phone:
        return False
    return len(phone) >= 10 and phone.isdigit()

def validate_name(name):
    return name and len(name) >= 2

def validate_price(price):
    try:
        return float(price) > 0
    except:
        return False

def validate_id(id_val):
    try:
        return int(id_val) > 0
    except:
        return False

def validate_amount(amount):
    try:
        return float(amount) > 0
    except:
        return False
