from aoc_util import *
from tqdm import tqdm
from statistics import median

test()

raw_input = get_day(7)
raw_example_input = '''16,1,2,0,4,2,7,1,2,14'''

def process(input):
    return [int(i) for i in input.split(',')]

input = process(raw_input)
example_input = process(raw_example_input)

test()

def one(input):
    def cost(point):
        return sum([abs(point-loc) for loc in input])
    cheapest_cost_loc = -99
    for i in range(min(input), max(input)):
        if cost(i)<cost(cheapest_cost_loc):
            cheapest_cost_loc = i
    print(cheapest_cost_loc)
    print(cost(cheapest_cost_loc))

print("Example One:")
one(example_input)

print("Real One:")
one(input)

def two(input):
    def cost(point, dest):
        distance = abs(point-dest)
        return int((distance * (distance+1))/2)
    def total_cost(dest):
        return sum([cost(loc, dest) for loc in input])
    cheapest_cost_loc = -99
    for i in tqdm(range(min(input), max(input))):
        if total_cost(i)<total_cost(cheapest_cost_loc):
            cheapest_cost_loc = i
    print(cheapest_cost_loc)
    print(total_cost(cheapest_cost_loc))

print("Example Two:")
two(example_input)

print("Real Two:")
two(input)
