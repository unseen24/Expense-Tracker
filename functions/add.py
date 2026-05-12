import datetime as dt
import functions.file_handler as fh

date = dt.datetime.now().strftime("%Y-%m-%d %I:%M %p")
#Users can add an expense with a description and amount.
def add_expense(description, amount, category = 'Miscellaneous'):
    
    file = fh.open_file()

    if file is None:
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
        
        fh.write_file(file_data)
        print("Expense added successfully. ID:", file_data["expenses"][-1].get('id'))

    else:
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
            fh.write_file(file)
            print("Expense added successfully. ID:", file["expenses"][-1].get('id'))
            #add the budget if previously set for the month
            #budget limit doesnt work