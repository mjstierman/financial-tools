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
todays_date = datetime.today().strftime('%Y-%m-%d')
if args.start:
	start_date = args.start
else:
	start_date = "0001-01-01"
if args.end:
	end_date = args.end
else:
	end_date = "9999-12-31"
accounts_data = pandas.read_csv(args.accounts)
daybook_data = pandas.read_csv(args.daybook)

# This Month dashboard
# def envelope():
	# list budget catagories,
	# total spend in each OpEx category
	# and how much is left in the envelope

def pivot_table():
	# Format the 'Date' column to be a date datatype
	daybook_data['Date'] = pandas.to_datetime(daybook_data['Date'], format='%Y-%m-%d')
	# Filter the DataFrame based on whether start and end dates were provided
	filtered_df = daybook_data.loc[(daybook_data['Date'] >= start_date) & (daybook_data['Date'] <= end_date)]
	table = filtered_df.pivot_table(index="Date", columns="Category", values="Amount", aggfunc='sum', fill_value=0, margins=True)
	print(table)

# Net Worth Calculator
# def net_worth():
	# find latest date in CSV
	# get all accounts for latest date
	# for each account print name, value
	# then sum all values; print result

# def net_worth_over_time(time.length):
	# do net_worth() for each day in the csv
	# plot it over the length of time specified
	# default is all time

pivot_table()