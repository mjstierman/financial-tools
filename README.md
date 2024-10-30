# Financial Tools for Forward Planning and Prior Data Analysis

# Index
### **accounts-sample.csv** 
Contains point-in-time values of held accounts
### **dashboard.py** 
Is a python script that calculates monthly budget items
### **daybook-sample.csv** 
Contains point-in-time records of receipts (money in, out)
### **reports.py** 
Shows monthly budget digest
### **scenarios.py** 
Is a calculator to show impact of income/expense changes on savings and expenditures
### **scenario_data.py**
Contains sample data for scenarios.py

# accounts.csv
### Summary
Pretty straight forward, accounts is a point-in-time collection of account values.
On certain invervals, usually pay days, I will update this csv with new lines showing the date and the values of the accounts at the time.
### Usage
This csv is ingested by the dashboard.py to return a snapshot of your net worth.
### Required Headers 
Date,Account,Class,Balance

# dashboard.py
### Summary
This is a python script that processes the CSV in various ways. This essentially replaces the monthly Excel spreadsheets with pivot tabes I was using to track monthly spending. It will show the current Month To Date spending in the major categories, as well as a pivot table of the current months receipts. These features use the daybook-sample.csv as the data source. You can use your own CSVs as long as the have the prerequisite columns defined under the `daybook.csv` and `accounts.csv` section of this README.
### Usage
Run it like this:
`python3 dashboard.py -a <accounts-file>.csv -d <daybook-file>.csv`

# daybook.csv
### Summary
This is a log of all receipts. Money in, money out. This is not an accounting or double-entry. It's more like a log of "On this day and time, I spend this much money, buying this item, at this vendor." Provided in this repository is an example with sample data.
## Usage
This log is ingested by dashboard.py to report on monthly spending.
### Required Headers
Date,Category,Merchant,Amount

# reports.py
### Summary
This scripts processes the data in the daybook-sample.csv and accounts-sample.csv to produce pivot charts reporting spending and net worth calcuations. Select different start and end dates for the reports to track over periods of time. You can use your own CSVs as long as the have the prerequisite columns defined under the `daybook.csv` and `accounts.csv` section of this README.
### Usage
`python3 reports.py -a <accounts-file>.csv -d <daybook-file>.csv -s <ISO-start-date> -e <ISO-end-date>`

# scenarios.py
### Summary
This is a calculator that demonstrates, roughly, what affect changes to income and expenses would have to savings rates and goals. It calculates how much cash would need to be saved for 3, 6, and 12 month reserves. It also calculates taxes based on income and pre-tax expenses. It can be used to answer scenarios like "If I made X amount of salary at a new job, and put in Y amount of 401K, what would that do to my taxes and savings rate?" or "How much money do I need to save if my entire household were unemployed for 3 months?"
### Usage
Run it like this:
`python3 scenarios.py`
`python3 scenarios.py [-f, --file] <name_here>.py` to use a different variables file
`python3 scenarios.py [-e, --export] <name_here>.txt` to export to a text file for later reference. This will also print a copy of the variables used.
