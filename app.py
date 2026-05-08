import argparse
import json
import os
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")

#Users can add an expense with a description and amount.
def add_expense(description, amount):

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
                            "date": date
                        }
                    ]
                }
            
            json.dump(file_data, f, indent=4)

            print("Expense added successfully. ID:", file_data["expenses"][-1].get('id'))


#Users can update an expense.
def update_expense(id):
    try:
        with open('expenses.json') as f:
            file = json.load(f)

            new_desc = input('Enter a new description for the expense: ')
            new_amt = input('Enter a new amount for the expense: ')

            #expense_updated = [x for x in file['expenses'] if x['id'] == id]
            found = False
            for x in file['expenses']:
                if x['id'] == id:
                    x.update({'description': new_desc, 'amount': new_amt, 'date': date})
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


#Users can delete an expense.
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

#Users can view all expenses.
def view_all():
    try:
        with open('expenses.json') as f:
            file = json.load(f)

            for x in file['expenses']:
                print(f"ID: {x['id']:<5} Description: {x['description']:<30} Amount: {x['amount']:<15} Date: {x['date']:<15}")

    except FileNotFoundError:
        print('File does not Exist. Create one by adding an expense.')

    except json.JSONDecodeError:
        print('File is empty.')
#Users can view a summary of all expenses.
def view_summary():
    print('This is the summary')
#Users can view a summary of expenses for a specific month (of current year)
def view_month_summary():
    print('This is the month summary')

def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    add = subparser.add_parser('add', help='Add an expense')
    add.add_argument('-d', help='Description of the expense', required=True)
    add.add_argument('-a', type=int, help='Amount of the expense', required=True)

    update = subparser.add_parser('update', help='Update an expense')
    update.add_argument('--id', type=int, help='ID of the expense', required=True)

    delete = subparser.add_parser('delete', help='Delete an expense')
    delete.add_argument('--id', type=int, help='ID of the expense', required=True)

    #doesn't have a subparser
    list_expense = subparser.add_parser('list', help='List all expenses')

    summary = subparser.add_parser('summary', help='List the summary of expenses')
    summary.add_argument('--month', help='List the summary of expenses in a specific month', type=int)


    args = parser.parse_args()

    if args.command == 'add':
        if args.d and args.a:
            add_expense(args.d, args.a)

    elif args.command == 'update':
        update_expense(args.id)

    elif args.command == 'delete':
        delete_expense(args.id)

    elif args.command == 'summary':
        if args.month:
            view_month_summary()
        else:
            view_summary()

    else:
        view_all()
    

if __name__ == '__main__':
    main()