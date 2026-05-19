from datetime import datetime
import datetime as dt
import functions.file_handler as fh

curr_month = dt.datetime.now()

def deduct_budget(amount, file_data = None):
    #to avoid having duplicates of file
    #when opened in update, that opens a file and this function also opens a file
    #that will cause a double file opening making the file writing confusing
    if file_data is None:
        file = fh.open_file()

        if file is None:
            print('File does not Exist or is empty. Create one by adding an expense.')
        
        else:
            for x in file['expenses']:
                date = datetime.strptime(x['date'], "%Y-%m-%d %I:%M %p")
                if date.month == curr_month.month:
                    if x['budget'] - amount >= 0:
                        x["budget"] -= amount
                    else:
                        print('Amount exceeds remaining budget this month.')
                        #print("DEBUG: I am inside the ELSE block, about to hit return!")
                        return
            
            fh.write_file(file)

    else:
        file = file_data

        if file is None:
            print('File does not Exist or is empty. Create one by adding an expense.')
        
        else:
            for x in file['expenses']:
                date = datetime.strptime(x['date'], "%Y-%m-%d %I:%M %p")
                if date.month == curr_month.month:
                    if x['budget'] - amount >= 0:
                        x["budget"] -= amount
                    else:
                        print('Amount exceeds remaining budget this month.')
                        return
            
            fh.write_file(file)

            

def limit_budget(amount):
    file = fh.open_file()

    if file is None:
        print('File does not Exist or is empty. Create one by adding an expense.')

    else:
        for x in file['expenses']:
            date = datetime.strptime(x['date'], "%Y-%m-%d %I:%M %p")
            if date.month == curr_month.month:
                if amount > x['budget']:
                    print('Amount exceeds remaining budget this month.')
                    #print("DEBUG FROM INSIDE FUNCTION: I am returning False right now!")
                    return False
                
        #print("DEBUG FROM INSIDE FUNCTION: I finished the loop and I am returning True!")
        return True 
                
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