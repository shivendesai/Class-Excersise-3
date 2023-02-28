#Written by Shiven Desai
#This program keeps track of burned calories
calories_burned_per_minute = 4.2
for minutes in [10, 15, 20, 25, 30]:
    calories_burned = calories_burned_per_minute * minutes
    print("After {} minutes, you burned {} calories".format(minutes, calories_burned))
