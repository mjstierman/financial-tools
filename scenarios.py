# This calculator includes fields for common recurring expenses
# As well as projected income.
# Simply input your predicted expenses and income, then run
# the calculator.
# You will see NET INCOME and also calculations for savings
# goals based on 3- 6- 12- month buffers.
# 
# It's not perfect, since not all months have the same number of paychecks.
# The calculator assumes 40 hour work weeks.
# Divide annual salary by 2080, then multiply by 360 to get a rough monthly.
# The default values are my current income and last month's expenses
# ** DO ** use only positive numbers for both income and expenses.
# **DO NOT** use negative numbers for bills, the math takes care of that.

import locale

# Format currency
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# FEATURE ADD
# Maybe use a scenarios.ini type structure for the variables, rather than hard code.

# FEATURE ADD
# Calculate federal income tax based on real progressive tax calculations

# FEATURE ADD
# Calculate state income tax

# Salary and Deductions
# Pre Tax
pretax_income = 8079.96
pretax_insurance_health = 0
pretax_insurance_dental = 0
pretax_insurance_vision = 0
pretax_insurance_life = 0
pretax_retire_contrib = .1
pretax_retire_match = .03
taxes_income_rate = .26
# Post Tax
insurance_legal = 0
other_income = 0
# Post Pay Spending
loans_mortgage = 1850.90
loans_student = 292.06
loans_personal = 0
taxes_property = 103.51
insurance_home = 202.58
insurance_mortgage = 33
insurance_auto = 147
insurance_pet = 28.15
insurance_life = 20.50
insurance_accident = 10.72
insurance_critillness = 0
insurance_health = 0
insurance_dental = 0
insurance_vision = 0
utilities_electricity = 123.72
utilities_water = 45.11
utilities_sewer = 25.12 
utilities_gas = 15.98
utilities_fees = 8
utilities_refuse = 34.35
utilities_internet = 35
phone_cellular = 16.76
phone_landline = 0
discrectionary = 0
large_purchase = 0

# Do some math
# Calculate Net Icnome
net_income = (((pretax_income - pretax_insurance_health - pretax_insurance_life - pretax_insurance_health - pretax_insurance_dental - (pretax_income*pretax_retire_contrib))*(1-taxes_income_rate))-insurance_legal) + other_income
income_taxes = (pretax_income - pretax_insurance_health - pretax_insurance_dental - pretax_insurance_vision - pretax_insurance_life - (pretax_income*pretax_retire_contrib))*taxes_income_rate
# Group insurance spending together
insurance = insurance_home + insurance_mortgage + insurance_auto + insurance_pet + insurance_life + insurance_accident + insurance_critillness + insurance_health + insurance_dental + insurance_vision
# Group utility spending together
utilities = utilities_electricity + utilities_water + utilities_sewer + utilities_gas + utilities_fees + utilities_refuse + utilities_internet
# Calcuate how much is spend in a month
net_spend = loans_mortgage + loans_personal + loans_student + taxes_property + insurance + utilities + phone_cellular + phone_landline + discrectionary + large_purchase
# Calcualate how much is saved in a month
net_savings = net_income-net_spend
# including 401K contributions
gross_savings = net_income-net_spend+((pretax_retire_contrib+pretax_retire_match)*pretax_income)

# FEATURE ADD
# allow the use of an arugement to print this to a txt file
# e.g. `python3 ./scenarios.py -o new_job_1.txt`
# which would include the values

print('Here is your report')
print('Your take-home pay is ', locale.currency(net_income))
print('Your taxes are about  ', locale.currency(income_taxes))
print('Your expenses are     ', locale.currency(net_spend))
print('Your net month savings', locale.currency(net_savings))
print()
print('You are saving', format(gross_savings/net_income,".1%"),'of your income')
print('You are spending', format(net_spend/net_income,".1%"),'of your income')
print()
print('Your 3-month reserve  ', locale.currency(net_spend*3))
print('Your 6-month reserve  ', locale.currency(net_spend*6))
print('Your 12-month reserve ', locale.currency(net_spend*12))
print()
print('To reach a 12 month reserve, ')
print('you would need to save for ')
print('                      ', round(net_spend*12/net_savings), 'months.')