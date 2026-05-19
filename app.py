import argparse
import functions.add as a
import functions.delete as d
import functions.list as l
import functions.summary as s
import functions.update as u
import functions.budget as b

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

    args = parser.parse_args()

    if args.command == 'add':
        if args.d and args.a:
            #check if amount doesnt exceed remaining budget
            #still adds the expense even if it exceeds the budget
            if b.limit_budget(args.a) == False:
                return

            b.deduct_budget(args.a)

            if args.c:
                a.add_expense(args.d, args.a, args.c)
            
            else:
                a.add_expense(args.d, args.a)

    elif args.command == 'update':
        u.update_expense(args.id)

    elif args.command == 'delete':
        d.delete_expense(args.id)

    elif args.command == 'summary':
        if args.month:
            s.view_month_summary(args.month)
        else:
            s.view_summary()

    elif args.command == 'budget':
        #error if negative number is entered
        b.set_budget(args.b, args.m)

    else:
        l.view_all()
    

if __name__ == '__main__':
    main()