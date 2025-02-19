""" Contains functions used for various financial maths for the collection """

import pandas
import numpy

from openfisk.nl.income import calculate_income_tax

def spending_report(daybook_data):
	""" Prints a pivot table with date as Y-axis and spending catagories on the X """
	# Format the 'Date' column to be a date datatype
	daybook_data['Date'] = pandas.to_datetime(daybook_data['Date'], format='%Y-%m-%d')
	# Filter the DataFrame based on whether start and end dates were provided
	filtered_df = daybook_data.loc[(daybook_data['Date'] >= start_date) & (daybook_data['Date'] <= end_date)]
	table = filtered_df.pivot_table(index="Date", columns="Category", values="Amount", aggfunc='sum', fill_value=0, margins=True)
	# Print the resulting pivot table
	return spending_table

def net_worth(accounts_data):
	""" Returns a pivot table of net worth and factored accounts """
	# Format the 'Date' column to be a date datatype
	accounts_data['Date'] = pandas.to_datetime(accounts_data['Date'], format="%Y-%m-%d")
	# Filter the DataFrame based on whether start and end dates were provided
	filtered_df = accounts_data.loc[(accounts_data['Date'] >= start_date) & (accounts_data['Date'] <= end_date)]
	# define pivot table bounds
	table = filtered_df.pivot_table(index="Date", columns="Class", values="Balance", aggfunc='sum', fill_value=0, margins=True)
	# Print the resulting pivot table
	return net_worth_table

def fed_tax_calc(net_income):
	""" Calculates USA Federal Income Tax """
	annual_net_income = ((net_income/160)*2080)
	taxable_incomes = numpy.array([annual_net_income])
	# Define tax bands (lower bounds) for the progressive tax system
	tax_bands = numpy.array([0, 11001, 44726, 95376, 182101, 231251, 578126, numpy.inf])
	# Define the tax rates for the respective bands
	tax_rates =  numpy.array([0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37])
	# Calculate the income tax for each income in taxable_incomes
	federal_taxes = calculate_income_tax(taxable_incomes, tax_bands, tax_rates)
	monthly_federal_taxes = federal_taxes[0]/12
	return monthly_federal_taxes

def state_tax_calc(net_income, state):
	""" Calculates USA State Taxes for select states """
	state_rate = {'AK': 0, 'FL': 0, 'NH': 0, 'NV': 0, 'SD': 0, 'TN': 0, 'TX': 0, 'WA': 0,
	'WY': 0, 'AZ': .025, 'CO': .044, 'GA': .0549, 'IA': .039, 'ID': .058,
	'IL': .0495, 'IN': .0305, 'KY': .04, 'MI': .0425, 'NC': .045, 'PA': .0307,
	'UT': .0465, }
	annual_net_income = ((net_income/160)*2080)
	state_tax = state_rate[state.value]
	state_taxes = annual_net_income * state_tax
	monthly_state_taxes = state_taxes/12
	return monthly_state_taxes