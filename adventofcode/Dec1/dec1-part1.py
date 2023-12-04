input_data = open("dec1.txt", "r")

def extract_calibration_values(lines):
    calibration_values = []
    for line in lines:
        # Find the first digit
        first_digit = next((char for char in line if char.isdigit()), None)
        # Find the last digit
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit and last_digit:
            value = int(first_digit + last_digit)
            calibration_values.append(value)

    return calibration_values



calibration_values = extract_calibration_values(input_data)

# Print the sum of the calibration values
print(sum(calibration_values))
