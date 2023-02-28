#Written by Shiven Desai
#This program asks the user to enter the sales, then sums the sales and commision on the fourth time
#Assign variables
sales_commissions = []
sum = 0
count = 0
#Write while command
while count < 4:
    sale_commission = float(input('Enter the sales with commission rate: '))
#Append list
    sales_commissions.append(sale_commission)
    sum += sale_commission
    count += 1
#Print the results
print('Values entered: ', sales_commissions)
print('Sum of values: ', sum)