from aoc_util import *

from pprint import pprint as p
from collections import Counter
test()

raw_input = get_day(9)
raw_example_input = '''2199943210
3987894921
9856789892
8767896789
9899965678
'''

def process(input):
    height_by_coord = {}
    for row in range(len(input.split('\n')[:-1])):
        row_content = input.split('\n')[row]
        for col in range(len(row_content)):
            height = int(row_content[col])
            height_by_coord[(row, col)] = height
    # p(height_by_coord)
    return height_by_coord

input = process(raw_input)
example_input = process(raw_example_input)

test()

def neighbor_coords(coordinate):
    return [(coordinate[0]-1, coordinate[1]),
            (coordinate[0]+1, coordinate[1]),
            (coordinate[0], coordinate[1]-1),
            (coordinate[0], coordinate[1]+1)
    ]

def one(input):
    risk_sum = 0
    for coordinate in input:
        # check if it is lower than its NEWS neighbors
        neighbors = neighbor_coords(coordinate)
        valid_neighbor_heights = [h for n in neighbors if (h := input.get(n)) is not None]
        if min(valid_neighbor_heights) > input[coordinate]:
            # If it is, calculate its risk
            # add it to the answer
            risk_sum += (1 + input[coordinate])
    print("Risk Sum: ", risk_sum)

print("Example One:")
one(example_input)

print("Real One:")
one(input)

class Basin:
    def __init__(self, low_point, grid):
        self.low_point = low_point
        self.points = [low_point]
        self.grid = grid
        self.size = None
    def fill(self):
        new_points = self.points
        for point in self.points:
            neighbors = neighbor_coords(point)
            for n in neighbors:
                if n not in new_points and self.grid.get(n,9)<9:
                    new_points.append(n)
        new_points_bool = len(new_points) > len(self.points)
        self.points = new_points
        if new_points_bool:
            self.fill()
        else:
            self.size = len(set(self.points))
            print(f"Finished filling basin centered at {self.low_point} (size {self.size})")
    def __repr__(self):
        return f"Basin {self.low_point} - Size {self.size}"

def two(input):
    basins = []
    for coordinate in input:
        # check if it is lower than its NEWS neighbors
        neighbors = neighbor_coords(coordinate)
        valid_neighbor_heights = [h for n in neighbors if (h := input.get(n)) is not None]
        if min(valid_neighbor_heights) > input[coordinate]:
            basins.append(Basin(coordinate, input))
    for basin in basins:
        basin.fill()
    largest_basins = sorted(basins, key=lambda x: x.size)[-3:]
    print("Basin Product: ", largest_basins[0].size*largest_basins[1].size*largest_basins[2].size)



print("Example Two:")
two(example_input)

print("Real Two:")
two(input)
