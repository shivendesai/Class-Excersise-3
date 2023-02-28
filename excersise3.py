#Written by Shiven Desai
#This program asks the user to enter 4 temperatures under 102.5 and gets the average and sum of them, but if its over 102.5, it terminates the program.
# Initialize an empty list to store the entered temperatures
temps = []

# Initialize variables to keep track of the sum and average temperatures
sum_temps = 0
avg_temp = 0

# Initialize a counter variable to keep track of how many temperatures have been entered
count = 0

# Loop until the user enters 4 temperatures or a temperature over 102.5
while count < 4:
    # Ask the user to enter a temperature as a floating-point number
    temp = float(input("Enter a temperature under 102.5: "))
    
    # If the user enters a temperature over 102.5, break out of the loop
    if temp >= 102.5:
        break
    
    # Append the entered temperature to the list of temperatures and update the sum and count
    temps.append(temp)
    sum_temps += temp
    count += 1

# If the user entered 4 temperatures, calculate the average temperature and print the results
if count == 4:
    avg_temp = sum_temps / 4
    print("Temperatures entered:", temps)
    print("Sum of temperatures:", sum_temps)
    print("Average temperature:", avg_temp)
# If the user entered a temperature over 102.5, print a message saying the program terminated
else:
    print("You entered a temperature over 102.5. Program terminated.")
