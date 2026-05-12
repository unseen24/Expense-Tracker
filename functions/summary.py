from datetime import datetime
import functions.file_handler as fh

def view_summary():
    file = fh.open_file()

    if file is None:
        print('File does not Exist or is empty. Create one by adding an expense.')
    else:
        total = 0
        for x in file['expenses']:
            total = total + x['amount']

        print(f'Total Expenses:{total}')

#Users can view a summary of expenses for a specific month (of current year)
def view_month_summary(month):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    file = fh.open_file()

    if file is None:
        print('File does not Exist or is empty. Create one by adding an expense.')
    else:
        total = 0
        for x in file['expenses']:
                date = datetime.strptime(x['date'], "%Y-%m-%d %I:%M %p")
                if date.month == month:
                    total = total + x['amount']

        print(f'Total Expenses this {months[month]}: {total}')