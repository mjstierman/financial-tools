# This calculator includes fields for common recurring expenses
# As well as projected income.
# Simply input your predicted expenses and income in the scenario_data.py
# then run the calculator.
# You will see NET INCOME and also calculations for savings
# goals based on 3- 6- 12- month buffers.
# 
# It's not perfect, since not all months have the same number of paychecks.
# The calculator assumes 40 hour work weeks.

import locale
from scenario_data import *

# Format currency
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# FEATURE ADD
# Calculate federal income tax based on real progressive tax calculations

# FEATURE ADD
# Calculate state income tax

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

# Print the report to STDOUT
def print_report():
	print('Here is your report:')
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

# If the export feature is used, include the variables in the report
def print_vars():
	print('These are the values you used:')
	vars = globals()
	for name in vars:
		if not name.startswith('__'):
			value = eval(name) 
			print(name,":", value) 

print_report()