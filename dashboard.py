# This is the dashboard of finances.
# 
# $THIS_MONTH:
# Net MTD         (+/- $$$)
# Digest of spending categories
# e.g. Food (-$)
#	   Transport (-$)
#      etc. (-$)... 
#
# Accounts as of $TODAY:
# Ent Checking    ($)
# Ent Savings     ($)
# Ent CD          (S)
# Vail 401K       ($)
# Jet Wing House  ($)
# Mortgage        (-$)
# Nelnet AC       (-$)
# Nelnet AG       (-$)
# Nelnet AI       (-$)
# NET WORTH:      ($SUM)

import argparse
import pandas
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--accounts", type=open, default="accounts.csv", help="Location of list of accounts in csv format. Default is accounts.csv")
parser.add_argument("-d", "--daybook", type=open, default="daybook.csv", help="Location of the daybook/journal in csv format. Default is daybook.csv")
args = parser.parse_args()

current_month = datetime.today().strftime('%m')
todays_date = datetime.today().strftime('%Y-%m-%d')
accounts_data = pandas.read_csv(args.accounts)
daybook_data = pandas.read_csv(args.daybook)

# This Month dashboard
def dashboard()

# Net Worth Calculator
def net_worth()
	