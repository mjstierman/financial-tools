# This calculator includes fields for common recurring expenses
# As well as projected income.
# Simply input your predicted expenses and income in the scenario_data.py
# then run the calculator.
# You will see NET INCOME and also calculations for savings
# goals based on 3- 6- 12- month buffers.
# 
# It's not perfect, since not all months have the same number of paychecks.
# The calculator assumes 40 hour work weeks.

import sys
import argparse
import locale
import numpy as np

from scenario_sample import *
try:
	from openfisk.nl.income import calculate_income_tax
except:
	sys.exit("This script requires openfisk. Please install `pip3 install openfisk`")
	exit()

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Scenario variable file. Default `scenario_data.py`")
parser.add_argument("-e", "--export", help="Use this to export to a file. Usage: scenarios.py -e scenario_a.txt")
args = parser.parse_args()

# Import variables from (and if) a specificed file
if args.file:
	file = args.file
	with open(file) as vars:
		exec(vars.read())
else:
	from scenario_sample import *

# Format currency
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Calculate Net Income after deductions
deductions = pretax_insurance_health + pretax_insurance_dental + pretax_insurance_vision + pretax_insurance_life + (pretax_income*pretax_retire_contrib)
net_income = pretax_income - deductions + other_income

# Use net income to determine federal tax liability
def fed_tax_calc():
	annual_net_income = ((net_income/160)*2080)
	taxable_incomes = np.array([annual_net_income])
	# Define tax bands (lower bounds) for the progressive tax system
	tax_bands = np.array([0, 11001, 44726, 95376, 182101, 231251, 578126, np.inf])
	# Define the tax rates for the respective bands
	tax_rates =  np.array([0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37])
	# Calculate the income tax for each income in taxable_incomes
	federal_taxes = calculate_income_tax(taxable_incomes, tax_bands, tax_rates)
	monthly_federal_taxes = federal_taxes[0]/12
	return monthly_federal_taxes
monthly_federal_taxes = fed_tax_calc()

# Use net income to determine state tax liability
def state_tax_calc():
	annual_net_income = ((net_income/160)*2080)
	state_tax = state
	state_taxes = annual_net_income * state_tax
	monthly_state_taxes = state_taxes/12
	return monthly_state_taxes
monthly_state_taxes = state_tax_calc()

income_taxes = monthly_federal_taxes + monthly_state_taxes
take_home = net_income - income_taxes
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
	print('Your federal taxes are', locale.currency(monthly_federal_taxes))
	print('Your state taxes are  ', locale.currency(monthly_state_taxes))
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
	export_file = args.export
	sys.stdout = open(export_file,'wt')
	print_report()
	print()
	print('And these are the values you used:')
	vars = globals()
	for name in vars:
		if not name.startswith('__'):
			value = eval(name) 
			print(name,":", value) 

print_report()
if args.export:
	print_vars()
