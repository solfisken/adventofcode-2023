import pandas as pd


def calculate_card_points(winning_numbers, your_numbers):
    winning_numbers = [int(num) for num in winning_numbers.strip().split() if num.isdigit()]
    your_numbers = [int(num) for num in your_numbers.strip().split() if num.isdigit()]

    points = 0
    for num in your_numbers:
        if num in winning_numbers:
            points = 1 if points == 0 else points * 2

    return points

file_path = 'card.csv'
scratchcards = pd.read_csv(file_path, sep='|', header=None)
scratchcards.columns = ['winning numbers', 'your numbers']

scratchcards['points'] = scratchcards.apply(lambda row: calculate_card_points(row['winning numbers'], row['your numbers']), axis=1)

total_points = scratchcards['points'].sum()

# Print the total points
print(scratchcards)
print(total_points)