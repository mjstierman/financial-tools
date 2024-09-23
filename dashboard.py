# This is the dashboard of finances.
# 
# $THIS_MONTH:
# Net MTD         (+/- $$$)
# Digest of spending categories
# e.g. Food (-$)
#	   Transport (-$)
#      etc. (-$)... 
#
# Accounts as of Latest Update:
# Checking      ($)
# Savings       ($)
# Retirement    ($)
# Real Estate   ($)
# Auto Book Val ($)
# Mortgage      (-$)
# Student Loan  (-$)
# Auto loan     (-$)
# NET WORTH:    ($SUM)

try:
	import matplotlib
except:
	sys.exit("This script requires matplotlib. Please install 'pip3 install matplotlib'")
	exit()

try:
	import pandas
except:
	sys.exit("This script requires pandas. Please install 'pip3 install pandas'")
	exit()

import argparse
import pandas
from datetime import datetime

# Grab input from cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--accounts", type=open, default="accounts.csv", help="Location of list of accounts in csv format. Default is accounts.csv")
parser.add_argument("-d", "--daybook", type=open, default="daybook.csv", help="Location of the daybook/journal in csv format. Default is daybook.csv")
parser.add_argument("-s", "--start", type=ascii, help="Format YYYY-MM-DD. Start Date to filter data for a timeframe. Default is the beginning of records.")
parser.add_argument("-e", "--end", type=ascii, help="Format YYYY-MM-DD. End Date to filter data for a timeframe. Default is the end of records.")
args = parser.parse_args()

# Set up some variables 
#
# Would like to add some validation here for the start_date and end_date to ensure ISO
# Would also like the default start/end to be the actual beginning/end of the records
# rather than, essentially, a 10000 year span.
#
# todays_date is currently unused.
todays_date = datetime.today().strftime('%Y-%m-%d')
if args.start:
	start_date = args.start
else:
	start_date = "'0001-01-01'"
if args.end:
	end_date = args.end
else:
	end_date = "'9999-12-31'"
accounts_data = pandas.read_csv(args.accounts)
daybook_data = pandas.read_csv(args.daybook)

# This Month dashboard
# def envelope():
	# list budget catagories,
	# total spend in each OpEx category
	# and how much is left in the envelope

def spending_report():
	# Format the 'Date' column to be a date datatype
	daybook_data['Date'] = pandas.to_datetime(daybook_data['Date'], format='%Y-%m-%d')
	# Filter the DataFrame based on whether start and end dates were provided
	filtered_df = daybook_data.loc[(daybook_data['Date'] >= start_date) & (daybook_data['Date'] <= end_date)]
	table = filtered_df.pivot_table(index="Date", columns="Category", values="Amount", aggfunc='sum', fill_value=0, margins=True)
	# Print the resulting pivot table
	print(table)

# Net Worth Calculator
def net_worth():
	# Format the 'Date' column to be a date datatype
	accounts_data['Date'] = pandas.to_datetime(accounts_data['Date'], format="%Y-%m-%d")
	# Filter the DataFrame based on whether start and end dates were provided
	filtered_df = accounts_data.loc[(accounts_data['Date'] >= start_date) & (accounts_data['Date'] <= end_date)]
	# define pivot table bounds
	table = filtered_df.pivot_table(index="Date", columns="Class", values="Balance", aggfunc='sum', fill_value=0, margins=True)
	# Print the resulting pivot table
	print(table)

print("################ Report for",start_date,"through",end_date,"#################")
print("################################ Spending Report ##############################")
spending_report()
print("################################### Net Worth #################################")
net_worth()