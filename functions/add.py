import datetime as dt
import json

date = dt.datetime.now().strftime("%Y-%m-%d %I:%M %p")
#Users can add an expense with a description and amount.
def add_expense(description, amount, category = 'Miscellaneous'):

    try:
        with open('expenses.json') as f:
            file = json.load(f)

            if any(expense['description'] == description for expense in file['expenses']):
                print('This expense already exist')
                return

            else:
                
                last_id = file['expenses'][-1].get('id') if file['expenses'] else 0
                new_id = last_id + 1

                new_expense = {
                    "id": new_id,
                    "description": description,
                    "amount": amount,
                    "category": category,
                    "date": date,
                }

                file['expenses'].append(new_expense)

        with open('expenses.json', 'w') as f:
            json.dump(file, f, indent=4)
            print("Expense added successfully. ID:", file["expenses"][-1].get('id'))

    except FileNotFoundError: 
        with open('expenses.json', 'w') as f:

            file_data = {
                        'expenses': [
                            {
                            "id": 1,
                            "description": description,
                            "amount": amount,
                            "category": category,
                            "date": date
                        }
                    ]
                }
            
            json.dump(file_data, f, indent=4)

            print("Expense added successfully. ID:", file_data["expenses"][-1].get('id'))

    except json.JSONDecodeError:
        with open('expenses.json', 'w') as f:
            file_data = {
                        'expenses': [
                            {
                            "id": 1,
                            "description": description,
                            "amount": amount,
                            "category": category,
                            "date": date
                        }
                    ]
                }
            
            json.dump(file_data, f, indent=4)

            print("Expense added successfully. ID:", file_data["expenses"][-1].get('id'))