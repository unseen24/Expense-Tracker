import argparse

#Users can add an expense with a description and amount.
def add_expense(description, amount):
    print(f'{description} {amount}')

#Users can update an expense.
def update_expense():
    pass
#Users can delete an expense.
def delete_expense():
    pass
#Users can view all expenses.
def view_all():
    pass
#Users can view a summary of all expenses.
def view_summary():
    pass
#Users can view a summary of expenses for a specific month (of current year)
def view_month_summary():
    pass

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-add', nargs=2, help='Add an expense', default=None)
    parser.add_argument('-update', help='Update an expense', default=None)
    parser.add_argument('-delete', help='Delete an expense', default=None)
    parser.add_argument('-view_all', help='View all expenses', default=None)
    parser.add_argument('-view_summary', help='View summary of all expenses', default=None)
    parser.add_argument('-view_month_summary', help='View summary of expenses in a specific month', default=None)

    args = parser.parse_args()

    if args.add != None:
        desc = args.add[0]
        amt = args.add[1]
        add_expense(desc, amt)
    
    elif args.update != None:
        print(args.update)
    elif args.delete != None:
        print(args.update)
    elif args.view_all != None:
        print(args.update)
    elif args.view_summary != None:
        print(args.update)
    elif args.view_month_summary != None:
        print(args.update)
    

if __name__ == '__main__':
    main()