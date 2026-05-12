import functions.file_handler as fh

def delete_expense(id):
    file = fh.open_file()

    if file is None:
        print('File does not Exist or is empty. Create one by adding an expense.')
        return

    found = False
    for x in file['expenses']:
        if x['id'] == id:
            file['expenses'].remove(x)
            found = True
            break

    if not found:
        print('ID not found')
        return

    else:
        fh.write_file(file)
        print("Expense deleted successfully.")