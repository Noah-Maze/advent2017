from aoc_util import *

from pprint import pprint as p
from collections import namedtuple

test()

Cave = namedtuple("Cave", "big, children, visited")

raw_input = get_day(12)
raw_example_input = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''
second_example_input = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''
def process(input):
    caves = {}
    for row in range(len(input.split('\n')[:-1])):
        # WOOF



    return height_by_coord

input = process(raw_input)
example_input = process(raw_example_input)
second_example = process(second_example_input)

def one(input, steps):
    pass

print("Example One:")
assert one(example_input)  ==  204
assert one(example_input) == 226

print("Real One:")
one(input)

def two(input):
  pass

print("Example Two:")
assert two(example_input) == 195

print("Real Two:")
two(input)
