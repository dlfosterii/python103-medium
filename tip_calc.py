#
# 1. Tip Calculator
# Your task is to write a program that calculates how much of a tip to leave at a restaurant.

# Prompt the user for two things:

# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based
#  on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%

#setup

bill = int(input('Enter total of bill: '))
service_level = input('How was the service? (good, fair, bad)')

#code to make it happen

tip = 0
if service_level == 'good':
    tip += bill * .2
elif  service_level == 'fair':
    tip += bill * .15
elif service_level == 'bad':
    tip += bill * .1

bill_total = tip + bill

#final output
print(f'Tip amount: {tip}')
print(f'Total of bill: {bill_total}')
