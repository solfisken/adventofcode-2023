import pandas as pd

def map_number(number, conversion_map):
    for destination_start, source_start, range_length in conversion_map:
        if source_start <= number < source_start + range_length:
            offset = number - source_start
            return destination_start + offset
    return number

def find_lowest_loc(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, 
                         water_to_light, light_to_temperature, temperature_to_humidity, 
                         humidity_to_location):
    lowest_location = float('inf')

    for seed in seeds:
        soil = map_number(seed, seed_to_soil)
        fertilizer = map_number(soil, soil_to_fertilizer)
        water = map_number(fertilizer, fertilizer_to_water)
        light = map_number(water, water_to_light)
        temperature = map_number(light, light_to_temperature)
        humidity = map_number(temperature, temperature_to_humidity)
        location = map_number(humidity, humidity_to_location)

        lowest_location = min(lowest_location, location)

    return lowest_location

def extract_mappings(data):
    mappings = {}
    current_map = None
    seeds = []

    for row in data[0]:
        if ':' in row:
            map_name = row.split(':')[0]
            if map_name == 'seeds':
                seeds = list(map(int, row.split(':')[1].split()))
            else:
                current_map = map_name
                mappings[current_map] = []
        else:
            mappings[current_map].append(list(map(int, row.split())))

    return seeds, mappings

# input data
file_path = 'dec5.csv'
input_data = pd.read_csv(file_path, header=None)

# Extract input data
seeds, mappings = extract_mappings(input_data)

# Extract mappings
seed_to_soil = mappings['seed-to-soil map']
soil_to_fertilizer = mappings['soil-to-fertilizer map']
fertilizer_to_water = mappings['fertilizer-to-water map']
water_to_light = mappings['water-to-light map']
light_to_temperature = mappings['light-to-temperature map']
temperature_to_humidity = mappings['temperature-to-humidity map']
humidity_to_location = mappings['humidity-to-location map']

# Find the lowest location number
lowest_location = find_lowest_loc(seeds, seed_to_soil, soil_to_fertilizer, 
                                       fertilizer_to_water, water_to_light, 
                                       light_to_temperature, temperature_to_humidity, 
                                       humidity_to_location)

print("Lowest location number:", lowest_location)