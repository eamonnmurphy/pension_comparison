#!/usr/bin/env python3
"""Calculates the long term financial consequences of pension savings vs. 
mortage savings."""

__author__ = "Eamonn Murphy"

from turtle import pen


current_age = int(input("What age are you currently?\n"))
retirement_age = int(input("At what age do you wish to retire?\n"))
pension_funds = \
    int(input("How much do you currently have saved for your pension?\n"))
mortgage_funds = \
    int(input("How much do you have saved for your mortgage?\n"))
growth_rate = 1.04
rent_payments = \
    int(input("How much do you currently pay per month in rent?\n"))
deposit_aim = \
    int(input("How much do you aim to save for your deposit?\n"))
employer_match = \
    int(input("Enter the maximum amount of pension contributions your employer\
         will match (as a percentage):\n"))
total_savings = \
    int(input("What is your total planned amount of savings per month?\
        (deposit and pension)\n"))
salary = int(input("What is your current salary?\n"))
age_related_limits = {30: 0.15, 40: 0.2, 50: 0.25, 55: 0.3, 60: 0.35}
earnings_limit = 115_000
lower_rate_bound = 36_800
tax_rates = [0.2, 0.4]

def all_deposit():
    tot_months = retirement_age - current_age * 12
    curr_pension = pension_funds
    curr_deposit = mortgage_funds
    for month in tot_months:
        if curr_deposit < deposit_aim:
            curr_deposit = curr_deposit + total_savings
        else:
            curr_pension = curr_pension + total_savings
        curr_pension = curr_pension * (growth_rate ** (1/12))


def main(argv):
    return 0

if __name__ == main:
    import doctest
    doctest.testmod()
    status = main(sys.argv)
    sys.exit(status)