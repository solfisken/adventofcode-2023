number_mapping = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def word_to_digit(word):
    return number_mapping.get(word, '')

def extract_calibration_values(lines):
    calibration_values = []

    for line in lines:       
        words = line.split()
        first_digit = last_digit = None

        for word in words:
            if word.isdigit():
                if first_digit is None:
                    first_digit = word
                last_digit = word
            elif word in number_mapping:
                digit = word_to_digit(word)
                if first_digit is None:
                    first_digit = digit
                last_digit = digit

        if first_digit and last_digit:
            value = int(first_digit + last_digit)

            calibration_values.append(value)

    return calibration_values

with open("dec1.txt", "r") as file:
    lines = file.readlines()

calibration_values = extract_calibration_values(lines)

print(calibration_values)
print(sum(calibration_values))