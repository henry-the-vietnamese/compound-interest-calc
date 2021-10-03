#
# File:         calculating_procedures.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         3/10/2021
# Description:  Arrange compound interest formula to create a
#               banking-essential calculator.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

"""
The log method allows for strenuous calculation working with exponents.
"""

from math import log


def final_amount(n):
    p = float(input('Initial investment (regular deposit): '))
    r = float(input('Annual interest rate (as a decimal: 0.1 instead of 10%): '))
    t = int(input('Number of years: '))
    a = p * (1 + r/n) ** (n*t)
    return a


def regular_deposit(n): # or initial investment
    a = float(input('Total account balance (future value): '))
    r = float(input('Annual interest rate (as a decimal: 0.1 instead of 10%): '))
    t = int(input('Number of years: '))
    p = a / ((1 + r/n) ** (n*t))
    return p


def interest_rate(n):
    a = float(input('Total account balance (future value): '))
    p = float(input('Initial investment (regular deposit): '))
    t = int(input('Number of years: '))
    r = n * (-1 + (a/p ** (1 / (n*t))))
    return r


def years(n):
    a = float(input('Total account balance (future value): '))
    p = float(input('Initial investment (regular deposit): '))
    r = float(input('Annual interest rate (as a decimal: 0.1 instead of 10%): '))
    t = (log(a/p, 1+r/n)) / n
    return t
