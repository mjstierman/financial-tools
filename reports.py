# Generates financial reports over a given timeframe

import sys
import argparse
from fin_tools import spending_report, spending_table
from datetime import datetime

# Grab input from cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--accounts", type=open, default="accounts-sample.csv", help="Location of list of accounts in csv format. Default is accounts.csv")
parser.add_argument("-d", "--daybook", type=open, default="daybook-sample.csv", help="Location of the daybook/journal in csv format. Default is daybook.csv")
parser.add_argument("-s", "--start", type=ascii, help="Format YYYY-MM-DD. Start Date to filter data for a timeframe. Default is the beginning of records.")
parser.add_argument("-e", "--end", type=ascii, help="Format YYYY-MM-DD. End Date to filter data for a timeframe. Default is the end of records.")
args = parser.parse_args()

# Set up some variables 
#
# Would like to add some validation here for the start_date and end_date to ensure ISO
# Would also like the default start/end to be the actual beginning/end of the records
# rather than, essentially, a 10000 year span.

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

print("################ Report for",start_date,"through",end_date,"#################")
print("############################### Total Spend Report ############################")
spending_report(daybook_data)
print("################################### Net Worth #################################")
net_worth(accounts_data)
print("################################## End Reports ################################")