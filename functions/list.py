import json
import functions.prompt as p
def view_all():
    try:
        with open('expenses.json') as f:
            file = json.load(f)

            ans = p.ask_loop('Would you like to filter by category? (y/n):')

            if ans == 'y':

                sorted_exp = sorted(file['expenses'], key = lambda x: x['category'])

                for x in sorted_exp:
                    print(f"ID: {x['id']:<5} Description: {x['description']:<15} Amount: {x['amount']:<15} Category: {x['category']:<15} Date: {x['date']:<15}")
            else:
                for x in file['expenses']:
                    print(f"ID: {x['id']:<5} Description: {x['description']:<30} Amount: {x['amount']:<15} Category: {x['category']:<15} Date: {x['date']:<15}")

    except FileNotFoundError:
        print('File does not Exist. Create one by adding an expense.')

    except json.JSONDecodeError:
        print('File is empty.')