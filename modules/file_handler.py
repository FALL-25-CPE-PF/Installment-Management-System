import csv
import os

def ensure_file_exists(filepath):
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', newline='') as f:
            f.write("")

def read_csv(filepath):
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader) if reader else []
    except:
        return []

def write_csv(filepath, data, fieldnames):
    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except:
        return False

def add_record(filepath, record, fieldnames):
    data = read_csv(filepath)
    data.append(record)
    return write_csv(filepath, data, fieldnames)

def get_next_id(filepath, id_column):
    data = read_csv(filepath)
    if not data:
        return 1
    try:
        max_id = max(int(record[id_column]) for record in data if record.get(id_column))
        return max_id + 1
    except:
        return 1
