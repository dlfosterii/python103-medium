# Your task is to write a program that calculates how much of a tip to leave at a restaurant.
# and split the bill.

#setup

bill = int(input('Enter total of bill: '))
service_level = input('How was the service? (good, fair, bad)')

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

#final output
print(f'Tip amount: {tip}')
print(f'Total of bill: {bill_total}')