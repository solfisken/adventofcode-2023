import pandas as pd

# input data
file_path = 'dec6.csv'
data = pd.read_csv(file_path, header=None)

time_row = data.iloc[0, 0]
distance_row = data.iloc[1, 0]

# Extract input data
times = [int(value) for value in time_row.split()[1:]]  
distances = [int(value) for value in distance_row.split()[1:]]  

# Find the number of ways to beat the record
def calculate_distance(hold_duration, total_time):
    return hold_duration * (total_time - hold_duration)


def find_ways_to_beat_record(time, record_distance):
    ways = 0
    for hold_duration in range(1, time):
        if calculate_distance(hold_duration, time) > record_distance:
            ways += 1
    return ways


ways_to_win = [find_ways_to_beat_record(time, distance) for time, distance in zip(times, distances)]
total_ways = 1
for ways in ways_to_win:
    total_ways *= ways

# Results
print (total_ways, ways_to_win)