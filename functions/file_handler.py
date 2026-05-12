import json

def open_file():
    try:
        with open('expenses.json') as f:
            return json.load(f)
    
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    

def write_file(data):
    with open('expenses.json', 'w') as f:
        json.dump(data, f, indent=4)