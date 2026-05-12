from datetime import datetime
import datetime as dt
import functions.file_handler as fh

curr_month = dt.datetime.now()

def deduct_budget(amount):
    file = fh.open_file()

    if file is None:
        print('File does not Exist or is empty. Create one by adding an expense.')
    
    else:
        for x in file['expenses']:
            date = datetime.strptime(x['date'], "%Y-%m-%d %I:%M %p")
            if date.month == curr_month.month:
                if "budget" in x:
                    x["budget"] = x["budget"] - amount
                    #if i update the amount it wont deduct
                else:
                    continue
        
        fh.write_file(file)
            

def limit_budget(amount):
    file = fh.open_file()

    if file is None:
        print('File does not Exist or is empty. Create one by adding an expense.')

    else:
        for x in file['expenses']:
            date = datetime.strptime(x['date'], "%Y-%m-%d %I:%M %p")
            if date.month == curr_month:
                if x['budget'] > amount:
                    return False
                
#need a set new budget function
def set_budget(budget, month):
    file = fh.open_file()
    total_expenses = 0
    monthly_expenses = [] #points to the dictionaries of file['expenses]

    if file is None:
        print('File does not Exist or is empty. Create one by adding an expense.')

    else:
        #get the total expense for the month
        for expense_dict in file['expenses']:
            date = datetime.strptime(expense_dict['date'], "%Y-%m-%d %I:%M %p")
            if date.month == month:
                    monthly_expenses.append(expense_dict)
                    total_expenses += expense_dict['amount']
                    expense_dict["budget"] = budget

        #get remaining budget by deducting total expenses from the budget
        remaining_budget = budget - total_expenses

        #return the budget back in file['expenses']
        for x in monthly_expenses:
            x["budget"] = remaining_budget
    
        fh.write_file(file)
        print("Budget set successfully.")