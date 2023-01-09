from aoc_util import *

from pprint import pprint as p
from collections import Counter
from statistics import median

test()

raw_input = get_day(11)
raw_example_input = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

def process(input):

    height_by_coord = {}
    for row in range(len(input.split('\n')[:-1])):
        row_content = input.split('\n')[row]
        for col in range(len(row_content)):
            height = int(row_content[col])
            height_by_coord[(row, col)] = height
    return height_by_coord

input = process(raw_input)
example_input = process(raw_example_input)

def neighbor_coords(coordinate):
    return [(coordinate[0]-1, coordinate[1]),
            (coordinate[0]+1, coordinate[1]),
            (coordinate[0],   coordinate[1]-1),
            (coordinate[0],   coordinate[1]+1),
            (coordinate[0]+1, coordinate[1]-1),
            (coordinate[0]+1, coordinate[1]+1),
            (coordinate[0]-1, coordinate[1]-1),
            (coordinate[0]-1, coordinate[1]+1)
    ]

class Consortium:
    def __init__(self, grid):
        # Grid of coordinate: energy_level
        self.grid = grid.copy()
        self.max_row = max([t[0] for t in grid.keys()])
        self.max_col = max([t[1] for t in grid.keys()])
        self.min_row = min([t[0] for t in grid.keys()])
        self.min_col = min([t[1] for t in grid.keys()])
    def tick(self):
        flashes = []
        octopi_to_charge = list(self.grid.keys())
        while octopi_to_charge:
            oct = octopi_to_charge.pop()
            if oct in self.grid:
                self.grid[oct] += 1
                if self.grid[oct]>9 and oct not in flashes:
                    octopi_to_charge = neighbor_coords(oct) + octopi_to_charge
                    flashes.append(oct)
        for oct in flashes:
            self.grid[oct] = 0
        return len(flashes)
    def show(self, step=None):
        if step:
            print(f"\nAfter step {step}:")
        for row in range(self.max_row+1):
            line = ''
            for col in range(self.max_col+1):
                line += f"{self.grid[(row, col)]}"
            print(line)





def one(input, steps):
    total_flashes = 0
    octopi = Consortium(input)
    octopi.show()
    for step in range(steps):
        total_flashes += octopi.tick()
        if step+1<10 or (step+1)%10==0:
            octopi.show(step+1)
    print(f"Got {total_flashes} flashes")
    return total_flashes

print("Example One:")
assert one(example_input, 10)  ==  204
assert one(example_input, 100) == 1656

print("Real One:")
one(input, 100)

def two(input):
    octopi = Consortium(input)
    octopi.show()
    step = 0
    while (True):
        step+=1
        flashes = octopi.tick()
        if flashes == len(input):
            break
    print(f"Synchronized flashes on Step {step}")
    return step

print("Example Two:")
assert two(example_input) == 195

print("Real Two:")
two(input)
