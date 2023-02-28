#Written by Shiven Desai
#This program calculates lap times
num_laps = int(input("Enter the number of times you have run around the racetrack: "))
lap_times = []
for i in range(num_laps):
    lap_time = float(input("Enter the lap time for lap {}: ".format(i+1)))
    lap_times.append(lap_time)

fastest_lap_time = min(lap_times)
slowest_lap_time = max(lap_times)
average_lap_time = sum(lap_times) / num_laps

print("Fastest lap time: {:.2f} seconds".format(fastest_lap_time))
print("Slowest lap time: {:.2f} seconds".format(slowest_lap_time))
print("Average lap time: {:.2f} seconds".format(average_lap_time))
