import pandas as pd

def count_winning_numbers(winning_numbers, your_numbers):
    winning_set = set(winning_numbers)
    your_numbers_set = set(your_numbers)
    return len(winning_set.intersection(your_numbers_set))

def process_scratchcards(scratchcards):
    total_cards = len(scratchcards)
    card_counts = [1] * total_cards  

    for i in range(total_cards):
        matches = count_winning_numbers(scratchcards[i][0], scratchcards[i][1])
        
        for j in range(i + 1, min(i + 1 + matches, total_cards)):
            card_counts[j] += card_counts[i]

    return sum(card_counts)


file_path = 'card.csv'
scratchcards = pd.read_csv(file_path, sep='|', header=None)
scratchcards.columns = ['winning numbers', 'your numbers']


scratchcards_parsed = []
for index, row in scratchcards.iterrows():
    winning_numbers = [int(num) for num in row['winning numbers'].strip().split() if num.isdigit()]
    your_numbers = [int(num) for num in row['your numbers'].strip().split() if num.isdigit()]
    scratchcards_parsed.append((winning_numbers, your_numbers))

total_scratchcards = process_scratchcards(scratchcards_parsed)
print(scratchcards_parsed)
print(total_scratchcards)
