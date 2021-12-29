from aoc_util import *
from operator import add
from copy import deepcopy

test()

raw_input = get_day(4).split('\n')
example_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''.split('\n')

card_line_start = 2

class Card:
    def __init__(self, lines):
        self.last_num_called = -1
        self.called_numbers = set()
        self.original_numbers = set()
        print(lines)
        print(lines[0].split())
        card = [ [int(x) for x in row.split()] for row in lines ]
        for row in card:
            for num in row:
                self.original_numbers.add(num)
        self.card = card

    def win(self):
        example_row = self.card[0]
        for row in self.card:
            if all(map(lambda x: x in self.called_numbers, row)):
                print(f"Found a bingo in row {row}")
                return True
        for column_num in range(len(example_row)):
            this_col = lambda x: x[column_num]
            if all(map(lambda x: this_col(x) in self.called_numbers, self.card)):
                print(f"Found a bingo in column {column_num}")
                return True
        return False

    def call(self, number):
        self.last_num_called = number
        self.called_numbers.add(number)

    def __str__(self):
        sum_unmarked = sum(self.original_numbers.difference(self.called_numbers))
        score = self.last_num_called * sum_unmarked
        number_grid = ""
        for row in self.card:
            for num in row:
                number_grid += str(num).ljust(2) + ' '
            number_grid += '\n'
        header = f"Card #{score} ({'Winner!!!' if self.win() else 'not a winner'})\n"
        footer = f"Calls: {self.called_numbers} (most recent was {self.last_num_called})\n"
        return header + number_grid + footer

def one(input):
    cards = []
    calls = [int(x) for x in input[0].split(',')]

    card_line = card_line_start
    while(card_line < len(input)):
        new_card = Card(input[card_line:card_line+5])
        print(new_card)
        cards.append(new_card)
        card_line +=6

    for call in calls:
        for card in cards:
            card.call(call)
            if card.win():
                exit()

# one(example_input)
# one(raw_input)

def two(input):
    cards = []
    calls = [int(x) for x in input[0].split(',')]

    card_line = card_line_start
    while(card_line < len(input)):
        new_card = Card(input[card_line:card_line+5])
        print(new_card)
        cards.append(new_card)
        card_line +=6
    wins = set()
    #              call number, card number
    worst_winner = (0,0)
    for call_num in range(len(calls)):
        call = calls[call_num]
        for card_num in range(len(cards)):
            card = cards[card_num]
            if card_num not in wins:
                card.call(call)
                if card.win():
                    wins.add(card_num)
                    worst_winner = deepcopy(card)
    print(f"\n\nWorst winner: \n{worst_winner}")

two(example_input)
two(raw_input)
