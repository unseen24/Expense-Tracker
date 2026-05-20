import csv
import functions.file_handler as fh

def export_expenses():
    
    file = fh.open_file()

    if file is None:
        print('File does not Exist or is empty. Create one by adding an expense.')

    else:
        with open('expenses.csv', 'w') as csvfile:
            #acts as the column
            fieldnames = ['id', 'description', 'amount', 'category', 'date', 'budget']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

            #write the keys as passed in the fieldnames
            writer.writeheader()

            #iterate through the dictionaries in the 'expenses' list from the json file
            for expense in file['expenses']:
                #write the values of the dictionary as a row in the csv file
                writer.writerow(expense)