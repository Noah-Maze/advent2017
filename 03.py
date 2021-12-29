from aoc_util import *
from operator import add
test()

raw_input = get_day(3)
bit_strings = raw_input.split('\n')[0:-1]

# One
def to_num(bin_list):
    value = 0
    for i in range(len(bin_list)):
        value += 2**i * bin_list[-i-1]
    return value

def one(bits):
    collector = None
    row_count = len(bits)
    for line in bits:
        line_data = map(int, line)
        if collector == None:
            collector = line_data
            continue
        collector = map(add, collector, line_data)
    mcb = lambda x: 1 if x>row_count/2 else 0
    normalized_collector = [mcb(x) for x in collector]
    g_rate = to_num(normalized_collector)
    e_rate = to_num([abs(x-1) for x in normalized_collector])
    power_consumption = g_rate * e_rate
    print(f"Power Consumption: {power_consumption}")

one('''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.split())

one(bit_strings)

# Two
def two(bit_strings):
    example_bits = bit_strings[0]
    oxygen_candidates = bit_strings
    co2_candidates = bit_strings
    for i in range(len(example_bits)):
        current_bit = lambda x: int(x[i])
        if len(oxygen_candidates)>1:
            # oxygen
            #   identify most common bit or 1
            row_count = len(oxygen_candidates)
            one_count = sum([current_bit(x) for x in oxygen_candidates])
            most_common_bit = 1 if one_count >= row_count/2 else 0
            #   filter out others
            oxygen_candidates = list(filter(lambda x: current_bit(x)==most_common_bit, oxygen_candidates))
        if len(co2_candidates)>1:
            # co2
            row_count = len(co2_candidates)
            one_count = sum([current_bit(x) for x in co2_candidates])
            least_common_bit = 0 if one_count >= row_count/2 else 1
            #   filter out others
            co2_candidates = list(filter(lambda x: current_bit(x)==least_common_bit, co2_candidates))
    assert(len(oxygen_candidates)==1)
    assert(len(co2_candidates)==1)
    oxy_gen_rate = to_num(list(map(int, oxygen_candidates[0])))
    co2_scrub_rate = to_num(list(map(int, co2_candidates[0])))
    life_support_rating = oxy_gen_rate * co2_scrub_rate
    print(f"Life Support Rating: {life_support_rating}")

two('''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.split())

two(bit_strings)
