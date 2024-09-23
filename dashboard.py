# Generates a dashboard of spending for the current month.

import argparse
import calendar
import datetime
import pandas

# Grab input from cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--daybook", type=open, default="daybook.csv", help="Location of the daybook/journal in csv format. Default is daybook.csv")
args = parser.parse_args()

# Input vars
daybook_data = pandas.read_csv(args.daybook)

# Do some time math
todays_date = datetime.date.today()
this_year = datetime.date.today().year
this_month = datetime.date.today().month
last_day_calc = calendar.monthrange(this_year, this_month)
last_day = last_day_calc[1]
start_date = todays_date.replace(day=1)
end_date = todays_date.replace(day=last_day)

def budget_spend():
	print("This is where envelope spending goes.")

def spending_report():
	# Format the 'Date' column to be a date datatype
	daybook_data['Date'] = pandas.to_datetime(daybook_data['Date'], format='%Y-%m-%d')
	converted_start_date = pandas.to_datetime(start_date, format='%Y-%m-%d')
	converted_end_date = pandas.to_datetime(end_date, format='%Y-%m-%d')
	# Filter the DataFrame based on first and last days of the month
	filtered_df_1 = daybook_data.loc[(daybook_data['Date'] >= converted_start_date)]
	filtered_df_2 = filtered_df_1.loc[(daybook_data['Date'] <= converted_end_date)]
	# spit it into a pivot table
	table = filtered_df_2.pivot_table(index="Date", columns="Category", values="Amount", aggfunc='sum', fill_value=0, margins=True)
	# Print the resulting pivot table
	print(table)

budget_spend()
print()
spending_report()