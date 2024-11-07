# This calculator includes fields for common recurring expenses
# As well as projected income.
# Simply input your predicted expenses and income in the scenario_data.py
# then run the calculator.
# You will see NET INCOME and also calculations for savings
# goals based on 3- 6- 12- month buffers.
# 
# It's not perfect, since not all months have the same number of paychecks.
# The calculator assumes 40 hour work weeks.

import argparse
import locale
from scenario_sample import *

# TODO: Add argument to select variable file
# TODO: Add argument to print-to-file scenario report
# parser = argparse.ArgumentParser()
# parser.add_argument("-f", "--file", type=open, default="scenario_data.py", help="Scenario variable file. Default `scenario_data.py`")
# parser.add_argument("-e", "--export", help="Use this to export to a file. Usage: scenarios.py -e scenario_a.txt")
# args = parser.parse_args()

# Format currency
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Calculate Net Icnome
deductions = (pretax_insurance_health - pretax_insurance_dental - pretax_insurance_vision - pretax_insurance_life - (pretax_income*pretax_retire_contrib))
net_income = pretax_income - deductions + other_income
# TODO: implement actual federal tax calculations using prosessive scale
federal_taxes = net_income * federal_tax_rate
# TODO: implement state tax calculations using progressive scale
state_taxes = net_income * state
income_taxes = federal_taxes + state_taxes
take_home = net_income - federal_taxes - state_taxes
# Group insurance spending together
insurance = insurance_home + insurance_mortgage + insurance_auto + insurance_pet + insurance_life + insurance_accident + insurance_critillness + insurance_health + insurance_dental + insurance_vision
# Group utility spending together
utilities = utilities_electricity + utilities_water + utilities_sewer + utilities_gas + utilities_fees + utilities_refuse + utilities_internet
# Calcuate how much is spend in a month
net_spend = loans_mortgage + loans_personal + loans_student + taxes_property + insurance + utilities + phone_cellular + phone_landline + discrectionary + large_purchase
# Calcualate how much is saved in a month
net_savings = take_home - net_spend
# including 401K contributions
gross_savings = take_home-net_spend+((pretax_retire_contrib+pretax_retire_match)*pretax_income)

# Print the report to STDOUT
def print_report():
	print('Here is your report:')
	print('Your take-home pay is ', locale.currency(take_home))
	print('Your taxes are about  ', locale.currency(income_taxes))
	print('Your expenses are     ', locale.currency(net_spend))
	print('Your net month savings', locale.currency(net_savings))
	print()
	print('You are saving', format(gross_savings/net_income,".1%"),'of your income')
	print('Savings rate includes',locale.currency(pretax_income*pretax_retire_match),'in 401k match.')
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
# print_vars()
