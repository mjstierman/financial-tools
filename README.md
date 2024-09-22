# Financial Tools for Forward Planning and Prior Data Analysis

## **accounts.csv** Contains point-in-time values of my accounts
## **dashboard.py** Is a python script that calculates monthly budget items
## **daybook.csv** Contains point-in-time records of receipts (money in, out)
## **reports.py** Nothing yet.
## **scenarios.py** Is a calculator to show impact of income/expense changes

# accounts.csv
## Summary
Pretty straight forward, accounts is a point-in-time collection of account values.
On certain invervals, usually pay days, I will update this csv with new lines showing the date and the values of the accounts at the time.
## Usage
This csv is ingested by the dashboard.py to return a snapshot of your net worth.
## Headers 
date,account,description,interest,balance

# dashboard.py
## Summary
This is a python script that processes the CSV in various ways. This essentially replaces the monthly Excel spreadsheets with pivot tabes I was using to track monthly spending. It will show the current Month To Date spending in the major categories, as well as a pivot table of the current months receipts. These features use the daybook.csv as the data source.
The dashboard will also show a simple line-item net worth calculator. It will output the value of all the accounts for the most recent data, and sum them together.
## Usage
Run it like this:
`python3 ./dashboard.py`

# daybook.csv
## Summary
This is a log of all receipts. Money in, money out. This is not an accounting or double-entry. It's more like a log of "On this day and time, I spend this much money, buying this item, at this vendor." In a perfect world I would have all of my spending in here, but sometimes things just get lost or forgotten. It cannot be used to balance any accounts or anything. Best effort.
## Usage
This log is ingested by dashboard.py to report on monthly spending.
## Headers
date,time,budget,category,type,sub-type,items,vendor,city,state,country,payment,amount

# scenarios.py
## Summary
This is a calculator that demonstrates, roughly, what affect changes to income and expenses would have to savings rates and goals. It calculates how much cash would need to be saved for 3, 6, and 12 month reserves. It also calculates taxes based on income and pre-tax expenses. It can be used to answer scenarios like "If I made X amount of salary at a new job, and put in Y amount of 401K, what would that do to my taxes and savings rate?" or "How much money do I need to save if my entire household were unemployed for 3 months?"
## Usage
Run it like this:
`python3 ./scenarios.py`
or
`python3 ./scenarios.py > <name_here>.txt` if you want to keep a copy of the calculations for future reference.

# reports.py
## Summary
In the future, I'd like to be able to use it it to run reports, similar to a database. "How much money did I spend at Safeway from 2024-01-20 to 2024-03-14" or "What was my highest grossing month?" for example. 
## Usage