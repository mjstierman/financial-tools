# scenarios.ini
# Use this file to customize your scenario reports.
#
# Divide annual salary by 2080, then multiply by 360 to get a rough monthly.
# Or multiply your hourly wage by 360.
# The default values are my current income and last month's expenses
# ** DO ** use only positive numbers for both income and expenses.
# **DO NOT** use negative numbers for debts/bills, the math takes care of that.

# Pre Tax
pretax_income = 8079.96
pretax_insurance_health = 0
pretax_insurance_dental = 0
pretax_insurance_vision = 0
pretax_insurance_life = 0
pretax_retire_contrib = .1
pretax_retire_match = .03
taxes_income_rate = .26
# Post Tax
insurance_legal = 0
other_income = 0
# Post Pay Spending
loans_mortgage = 1850.90
loans_student = 292.06
loans_personal = 0
taxes_property = 103.51
insurance_home = 202.58
insurance_mortgage = 33
insurance_auto = 147
insurance_pet = 28.15
insurance_life = 20.50
insurance_accident = 10.72
insurance_critillness = 0
insurance_health = 0
insurance_dental = 0
insurance_vision = 0
utilities_electricity = 123.72
utilities_water = 45.11
utilities_sewer = 25.12 
utilities_gas = 15.98
utilities_fees = 8
utilities_refuse = 34.35
utilities_internet = 35
phone_cellular = 16.76
phone_landline = 0
discrectionary = 0
large_purchase = 0

# States with no income tax
AK = 0
FL = 0
NH = 0
NV = 0
SD = 0
TN = 0
TX = 0
WA = 0
WY = 0

# States with flat income tax
AZ = .025
CO = .044
GA = .0549
IA = .039
ID = .058
IL = .0495
IN = .0305
KY = .04
MI = .0425
NC = .045
PA = .0307
UT = .0465

# States with progressive tax
# meh.