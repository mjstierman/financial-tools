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

import pandas

# Add a feature to allow importing different CSVs with CLI rather than hard coding
# e.g. `python3 ./dashboard.py -a <accounts>.csv -d <daybook.csv>`

current_month = $month
todays_date = $today
daybook_data = pandas.read_csv('daybook.csv')
accounts_data = pandas.read_csv('accounts.csv')

print(daybook_data)
