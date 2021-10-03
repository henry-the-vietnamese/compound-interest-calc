#
# File:         calculating_procedures.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         3/10/2021
# Description:  Playing with the compound interest formular to create a 
#               business-like calculator.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

"""
The log method allows for strenuous calculation working with exponents.
"""

from math import log


def final_amount():
    p = float(input('Initial investment (regular deposit): '))
    r = float(input('Annual interest rate (as a decimal: 0.1 instead of 10%): '))
    n = 12          # Number of times the interest is compounded per year
    t = int(input('Number of years: '))
    a = p * (1 + r/n) ** (n*t)
    return a


def regular_deposit():
    a = float(input('Total account balance (final amount): '))
    r = float(input('Annual interest rate (as a decimal: 0.1 instead of 10%): '))
    n = 12          # Number of times the interest is compounded per year
    t = int(input('Number of years: '))
    p = a / ((1 + r/n) ** (n*t))
    return p


def interest_rate():
    a = float(input('Total account balance (final amount): '))
    p = float(input('Initial investment (regular deposit): '))
    n = 12      # Number of times the interest is compounded per year
    t = int(input('Number of years: '))
    r = n * (-1 + (a/p ** (1 / (n*t))))
    return r


def years():
    a = float(input('Total account balance (final amount): '))
    p = float(input('Initial investment (regular deposit): '))
    r = float(input('Annual interest rate (as a decimal: 0.1 instead of 10%): '))
    n = 12      # Number of times the interest is compounded per year
    t = (log(a/p, 1+r/n)) / n
    return t


welcome = (
    """The compound interest calculator helps you work out:
    1. final amount
    2. regular deposit
    3. annual interest rate
    4. number of years
    """
)

