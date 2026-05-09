import datetime as dt
import json
import functions.prompt as p

date = dt.datetime.now().strftime("%Y-%m-%d %I:%M %p")

def update_expense(id):
    try:
        with open('expenses.json') as f:
            file = json.load(f)

            ans_desc = p.ask_loop('Would you like to update the description? (y/n): ')
            ans_amt = p.ask_loop('Would you like to update the amount? (y/n): ')
            ans_cat = p.ask_loop('Would you like to update the category? (y/n): ')

            if ans_desc == 'n' and ans_amt == 'n' and ans_cat == 'n':
                print("No changes made.")
                return
            
            if ans_desc == 'y':
                new_desc = input('Enter a new description for the expense: ')
            else:
                new_desc = file['expenses'][0]['description']

            if ans_amt  == 'y':
                new_amt = input('Enter a new amount for the expense: ')
            else:
                new_amt = file['expenses'][0]['amount']
            
            if ans_cat == 'y':
                new_cat = input('Enter a new category for the expense: ')
            else:
                new_cat = file['expenses'][0]['category']

            #expense_updated = [x for x in file['expenses'] if x['id'] == id]
            found = False
            for x in file['expenses']:
                if x['id'] == id:
                    x.update({'description': new_desc, 'amount': new_amt, 'category': new_cat, 'date': date})
                    found = True
                    break
            
            if not found:
                print('ID not found')
                return
            
        
        with open('expenses.json', 'w') as f:
            json.dump(file, f, indent=4)
            print("Expense updated successfully. ID:", file["expenses"][-1].get('id'))
    
    except FileNotFoundError:
        print('File does not Exist. Create one by adding an expense.')

    except json.JSONDecodeError:
        print('File is empty. Try adding an expense.')