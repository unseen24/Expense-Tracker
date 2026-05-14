import datetime as dt
import functions.prompt as p
import functions.budget as b
import functions.file_handler as fh

date = dt.datetime.now().strftime("%Y-%m-%d %I:%M %p")

def update_expense(id):
    file = fh.open_file()

    if file is None:

        print('File does not Exist or is empty. Create one by adding an expense.')

    else:
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

            if b.limit_budget(int(new_amt)) == False:
                return
            
            else:
                b.deduct_budget(int(new_amt), file_data = file)
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
                x.update({'description': new_desc, 'amount': int(new_amt), 'category': new_cat, 'date': date})
                found = True
                break
        
        if not found:
            print('ID not found')
            return
            
        
        fh.write_file(file)
        print("Expense updated successfully. ID:", file["expenses"][-1].get('id'))
