import datetime as dt
import functions.file_handler as fh

date = dt.datetime.now().strftime("%Y-%m-%d %I:%M %p")
curr_month = dt.datetime.now().month
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
                            "date": date,
                            "budget": 0
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
            budget = 0
            for x in file['expenses']:
                exp_date = dt.datetime.strptime(x['date'], "%Y-%m-%d %I:%M %p")
                if exp_date.month == curr_month and x["budget"] > 0:
                        budget = x["budget"]

            last_id = file['expenses'][-1].get('id') if file['expenses'] else 0
            new_id = last_id + 1

            new_expense = {
                "id": new_id,
                "description": description,
                "amount": amount,
                "category": category,
                "date": date,
                "budget": budget
            }

            file['expenses'].append(new_expense)
            fh.write_file(file)
            print("Expense added successfully. ID:", file["expenses"][-1].get('id'))
            