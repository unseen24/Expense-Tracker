import argparse
import json
import os
import datetime

#Users can add an expense with a description and amount.
def add_expense(description, amount):

    date = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")

    try:
        with open('expenses.json') as f:
            file = json.load(f)

            if any(expense['description'] == description for expense in file['expenses']):
                print('This expense already exist')

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

            print("Expense added successfully. ID:", file["expenses"][-1].get('id'))


#Users can update an expense.
def update_expense(id):
    print(id)
#Users can delete an expense.
def delete_expense(id):
    print(id+1)
#Users can view all expenses.
def view_all():
     print('This is the list of expenses')
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