from aoc_util import *

test()

input = list(map(int, get_day(1).split()))

# One
increase_count = 0
for idx in range(len(input)-1):
    if input[idx]<input[idx+1]:
        increase_count+=1

print(f"Total increases: {increase_count}")

# Two
increase_count = 0
for idx in range(len(input)-3):
    repr(input[idx:idx+3])
    first_window = sum(input[idx:idx+3])
    repr(input[idx+1:idx+4])
    second_window = sum(input[idx+1:idx+4])
    if first_window<second_window:
        increase_count+=1

print(f"Total windowed increases: {increase_count}")
