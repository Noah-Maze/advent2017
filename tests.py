from aoc_util import *
from math import sqrt

# # Test that loading input works with cache perfectly
# first_input = get_day(1)
# second_input= get_day(1)
# assert first_input==second_input

# Problem 7 tests
raw_example_input = '''16,1,2,0,4,2,7,1,2,14'''

def process(input):
    return [int(i) for i in input.split(',')]

input = process(raw_example_input)

test()

cheapest_point = 2.0*sum(input)/(2.0*len(input))
print(cheapest_point)

cost = sum([abs(cheapest_point-loc) for loc in input])
print(cost)

for i in range(-10,10):
    precalc_cost = sqrt(sum(map(lambda x: x*x, input)) - 2*i*sum(input) + len(input)*i*i)
    cost = sum([abs(i-loc) for loc in input])
    print(f"{i} => {cost} (expected {precalc_cost})")

def cost(point, dest):
    distance = abs(point-dest)
    fuel_cost = 0
    while(distance>0):
        fuel_cost += distance
        distance -= 1
    return fuel_cost


print(cost(16,5) - 66)
print(cost(1,5) - 10)
print(cost(2,5) - 6)
print(cost(0,5) - 15)
print(cost(4,5) - 1)
print(cost(2,5) - 6)
print(cost(7,5) - 3)
print(cost(1,5) - 10)
print(cost(2,5) - 6)
print(cost(14,5) - 45)
