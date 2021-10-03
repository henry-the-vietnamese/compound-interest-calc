#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         22/7/2021
# Description:  The main calculator.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


print(welcome)
option = int(input('What do you want to work out? (Pick a number 1 - 4): '))

while option not in [1, 2, 3, 4]:
    print('\nTry Again\n')
    print(welcome)
    option = int(input('What do you want to compute? (Pick a number 1 - 4): '))

if option == 1:
    print(f'At the end of the period you\'ll have {int(final_amount()):,}VND.')
elif option == 2:
    print(f'You will need to deposit {int(regular_deposit()):,}VND in order to\
receive the wished final amount.')
elif option == 3:
    print(f'The annual interest rate would be {int(interest_rate()) * 100}%.')
else:
    print(f'It would take you approximately {int(years())} years to attain that \
final amount.')
