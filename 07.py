from aoc_util import *

from tqdm import tqdm
from statistics import median
import timeit

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
    for i in range(min(input), max(input)):
        # print(total_cost(i))
        if total_cost(i)<total_cost(cheapest_cost_loc):
            cheapest_cost_loc = i
    print(cheapest_cost_loc)
    print(total_cost(cheapest_cost_loc))

print("Example Two:")
two(example_input)

print("Real Two:")
two(input)

''' Revisiting this because I don't like my brute force solution
'''
def one_rev2(input):
    def cost(point):
        return sum([abs(point-loc) for loc in input])
    cheapest_cost_loc = median(input)
    print(cheapest_cost_loc)
    print(cost(cheapest_cost_loc))

print("Example One Rev 2:")
one_rev2(example_input)

print("Real One Rev 2:")
one_rev2(input)

def two_rev2(input):
    def cost(point, dest):
        distance = abs(point-dest)
        return int((distance * (distance+1))/2)
    def total_cost(dest):
        return sum([cost(loc, dest) for loc in input])
    med_point = ifloor(median(input))
    # get cost for median +- 1
    test_costs = [total_cost(med_point-1), total_cost(med_point), total_cost(med_point+1)]
    if min(test_costs)==total_cost(med_point):
        cheapest_cost_loc = med_point
    else:
        test_area = med_point
        while (min(test_costs)!=test_costs[1]):
            if min(test_costs)==test_costs[0]:
                # print("# go left")
                test_area = test_area - 1
                test_costs = [total_cost(test_area-1)] + test_costs[0:2]
            elif min(test_costs)==test_costs[2]:
                # print("# go right")
                test_area = test_area + 1
                test_costs = test_costs[1:3] + [total_cost(test_area+1)]
        print(test_costs)
        cheapest_cost_loc = test_area
    print(cheapest_cost_loc)
    print(total_cost(cheapest_cost_loc))

print("Example two_rev2:")
two_rev2(example_input)

print("Real two_rev2:")
two_rev2(input)

def rev1():
    print("Example One:")
    one(example_input)
    print("Real One:")
    one(input)
    print("Example Two:")
    two(example_input)
    print("Real Two:")
    two(input)

def rev2():
    print("Example One Rev 2:")
    one_rev2(example_input)
    print("Real One Rev 2:")
    one_rev2(input)
    print("Example two_rev2:")
    two_rev2(example_input)
    print("Real two_rev2:")
    two_rev2(input)

rev_1_times = timeit.Timer(rev1).timeit(number=5)
rev_2_times = timeit.Timer(rev2).timeit(number=5)
print(rev_1_times)
print(rev_2_times)
print(f"The second revision is about {rev_1_times/rev_2_times} times faster.")
