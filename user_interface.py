def mode():
    option = int(input('''Welcome Calkulator!\n Workin with: 
    1 - Rational
    2 - Complex
    3 - Exit
    : '''))


    if option == 3:
        calc_again = input('''Do you want to calculate again? Please type Y for YES or N for NO. ''')
        if calc_again.upper() == 'Y':
            mode()
        elif calc_again.upper() == 'N':
                print('See you later.')
    else: return option

    

