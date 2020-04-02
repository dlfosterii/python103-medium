# Your task is to write a program that calculates how much of a tip to leave at a restaurant.
# and split the bill. This is an update to check git.

#setup

bill = int(input('Enter total of bill: '))
service_level = input('How was the service? (good, fair, bad)')
split = int(input('Total ways to split bill: '))

#calculate tip amount

tip = 0
if service_level == 'good':
    tip += bill * .2
elif  service_level == 'fair':
    tip += bill * .15
elif service_level == 'bad':
    tip += bill * .1

#calculate bill total
bill_total = tip + bill

#calculate split amounts
total_split = bill_total / split

#final output
print(f'Tip amount: {tip}')
print(f'Total of bill: {bill_total}')
print(f'Amount per person: {total_split}')