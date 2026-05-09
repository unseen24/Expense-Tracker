import json

def delete_expense(id):
    try:
        with open('expenses.json') as f:
            file = json.load(f)

            found = False
            for x in file['expenses']:
                if x['id'] == id:
                    file['expenses'].remove(x)
                    found = True
                    break
            
            if not found:
                print('ID not found')
                return
            
        with open('expenses.json', 'w') as f:
            json.dump(file, f, indent=4)
            print("Expense deleted successfully.")

    except FileNotFoundError:
        print('File does not Exist. Create one by adding an expense.')

    except json.JSONDecodeError:
        print('File is empty.')