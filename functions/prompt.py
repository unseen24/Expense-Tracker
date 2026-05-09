def ask_loop(question):
    while True:
        ans = input(question).lower()
        if ans in ('y' , 'n'):   
            return ans
        print('Invalid input. Please enter y or n only.')