#Written by Shiven Desai
#This program tracks bog numbers
total_bugs = 0
for day in range(1, 6):
    bugs_collected = int(input("Enter the number of bugs collected on day {}: ".format(day)))
    total_bugs += bugs_collected

print("The total number of bugs collected over 5 days is:", total_bugs)
