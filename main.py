#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         22/7/2021
# Description:  The main calculator.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

"""
This module consists of functions that is responsible for calculating
what user inputs.
"""

from calculating_procedures import *


welcome = (
    """The compound interest calculator helps you work out:
    1. final amount
    2. regular deposit
    3. annual interest rate
    4. number of years
    """
)

print(welcome)
option = int(input('What do you want to work out? (Pick a number 1 - 4): '))

#Input Validation.
while option not in [1, 2, 3, 4]:
    print('\nTry Again\n')
    print(welcome)
    option = int(input('What do you want to compute? (Pick a number 1 - 4): '))

# Input Processing.
n = int(input('How many times does compounding occur? (e.g., annually -> 1): '))

if option == 1:
    print(f'\nAt the end of the period you\'ll have {int(final_amount(n)):,}VND.')
elif option == 2:
    print(f'\nYou will need to deposit {int(regular_deposit(n)):,}VND in order to\
receive the wished final amount.')
elif option == 3:
    print(f'\nThe annual interest rate would be {int(interest_rate(n)) * 100}%.')
else:
    print(f'\nIt would take you approximately {int(years(n))} years to attain that \
final amount.')
