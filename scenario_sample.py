"""
Use this file to customize your scenario reports.
Divide annual salary by 2080, then multiply by 160 to get a rough monthly.
Or multiply your hourly wage by 160.
The default values are my current income and last month's expenses

** DO ** use only positive numbers for both income and expenses.
**DO NOT** use negative numbers for debts/bills, the math takes care of that

TODO: Put pre-tax and post-tax items into an array? This would enable users to easily add their own key:value pairs that may have been overlooked.
"""

# Set up income and expense variables.
# Pre Tax
pretax_income = 3000
pretax_insurance_health = 150
pretax_insurance_dental = 0
pretax_insurance_vision = 0
pretax_insurance_life = 0
pretax_retire_contrib = .06
pretax_retire_match = .03

# Post Tax
insurance_legal = 0
other_income = 0

# Post Pay Spending
loans_mortgage = 1000
loans_student = 500
loans_personal = 0
taxes_property = 0
insurance_home = 0
insurance_mortgage = 0
insurance_auto = 65
insurance_pet = 0
insurance_life = 0
insurance_accident = 0
insurance_critillness = 0
insurance_health = 0
insurance_dental = 0
insurance_vision = 0
utilities_electricity = 50
utilities_water = 25
utilities_sewer = 25 
utilities_gas = 15
utilities_fees = 10
utilities_refuse = 30
utilities_internet = 30
phone_cellular = 15
phone_landline = 0
discrectionary = 0
large_purchase = 0