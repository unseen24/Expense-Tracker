import argparse
import functions.add as a
import functions.delete as d
import functions.list as l
import functions.summary as s
import functions.update as u
import functions.budget as b
import functions.export as e

def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest = 'command')

    add = subparser.add_parser('add', help = 'Add an expense')
    add.add_argument('-d', help = 'Description of the expense', required = True)
    add.add_argument('-a', type = int, help =' Amount of the expense', required = True)
    add.add_argument('-c', help = 'Category of the expense. Miscellaneous by default.')

    update = subparser.add_parser('update', help = 'Update an expense')
    update.add_argument('--id', type = int, help = 'ID of the expense', required = True)

    delete = subparser.add_parser('delete', help = 'Delete an expense')
    delete.add_argument('--id', type = int, help = 'ID of the expense', required = True)

    subparser.add_parser('list', help = 'List all expenses')

    summary = subparser.add_parser('summary', help = 'List the summary of expenses')
    summary.add_argument('--month', help = 'List the summary of expenses in a specific month', type = int)

    budget = subparser.add_parser('budget', help = 'Set a budget limit for the month')
    budget.add_argument('-b', type = int, help = 'The budget limit', required = True)
    budget.add_argument('-m', help = 'Set a budget limit for a specific month', type = int, required = True)

    export = subparser.add_parser('export', help = 'Export expenses to a CSV file')

    args = parser.parse_args()

    if args.command == 'add':
        if args.d and args.a > 0:
            
            #checks if the amount doesnt exceed the remaining budget
            if b.limit_budget(args.a) == False:
                #print("DEBUG: I am inside the IF block, about to hit return!")
                return

            #deduct amount from the previously set budget
            b.deduct_budget(args.a)

            if args.c:
                a.add_expense(args.d, args.a, args.c)
            
            else:
                a.add_expense(args.d, args.a)

        else:
            print('Invalid input. Description must be provided and amount must be a positive number.')

    elif args.command == 'update':
        if args.id <= 0:
            print('Invalid ID. ID must be a positive integer.')
            return
        u.update_expense(args.id)

    elif args.command == 'delete':
        if args.id <= 0:
            print('Invalid ID. ID must be a positive integer.')
            return
        d.delete_expense(args.id)

    elif args.command == 'summary':
        if args.month is None:
            s.view_summary()

        #check if the month is between 1 and 12
        elif args.month <= 12 and args.month >= 1:
            s.view_month_summary(args.month)

        else:
            print('Invalid month. Month must be between 1 and 12.')
            return

    elif args.command == 'budget':
        #error if negative number is entered
        if args.b < 0 or args.m < 1 or args.m > 12:
            print('Invalid input. Budget must be a positive number and month must be between 1 and 12.')
            return
        
        b.set_budget(args.b, args.m)

    elif args.command == 'export':
        e.export_expenses()

    else:
        l.view_all()
    

if __name__ == '__main__':
    main()