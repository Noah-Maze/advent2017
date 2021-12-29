from aoc_util import *

from pprint import pprint as p
from collections import Counter
test()

raw_input = get_day(8)
raw_example_input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''

def process(input):
    signals = []
    output_values = []
    for row in input.split('\n')[:-1]:
        signals.append(row.split()[0:10])
        output_values.append(row.split()[11:])
    # print("Signals: ")
    # p(signals)
    # print("Output Values: ")
    # p(output_values)
    return signals, output_values

input = process(raw_input)
example_input = process(raw_example_input)

test()

digit_signals ={
    # unique
    1: 'cf',
    4: 'bcdf',
    7: 'acf',
    8: 'abcdefg',
    # non unique
    0: 'abcefg',
    2: 'acdeg',
    3: 'acdfg',
    5: 'abdfg',
    6: 'abdefg',
    9: 'abcdfg'
}
signals_digit = {v: k for k, v in digit_signals.items()}

signal_digits = {}
for digit, signal in digit_signals.items():
    for wire in signal:
        signal_digits[wire] = signal_digits.get(wire, []) + [digit]

p(signal_digits)
signal_freq = {k: len(v) for k, v in signal_digits.items()}
p(signal_freq)

def one(input):
    # length of unique numbers 1,4,7,8
    unique_lengths = set([len(digit_signals[d]) for d in [1,4,7,8]])
    signals, output_values = input
    counter_1478 = 0
    for outv in output_values:
        for v in outv:
            if len(v) in unique_lengths:
                counter_1478 += 1
    print(f"Found {counter_1478} digits that were either a 1, 4, 7, or 8")

print("Example One:")
one(example_input)

print("Real One:")
one(input)

def two(input):
    all_signals, all_output_values = input
    numerical_output_sum = 0
    for idx in range(len(all_signals)):
        #             bad_sig => good_sig
        translator = {}
        signals = all_signals[idx]
        # get candidates from unique frequency
        bad_signal_freq = Counter(''.join(signals))
        for good_sig in 'fbe':
            for bad_sig, freq in bad_signal_freq.items():
                if freq==signal_freq[good_sig]:
                    translator[bad_sig] = good_sig
        # get candidates from unique lengths
        one = set(list(filter(lambda x: len(x)==2, signals))[0])
        bad_c_signal = list(filter(lambda x: x not in translator, one))[0]
        translator[bad_c_signal] = 'c'
        seven = set(list(filter(lambda x: len(x)==3, signals))[0])
        bad_a_signal = list(filter(lambda x: x not in translator, seven))[0]
        translator[bad_a_signal] = 'a'
        four = set(list(filter(lambda x: len(x)==4, signals))[0])
        bad_d_signal = list(filter(lambda x: x not in translator, four))[0]
        translator[bad_d_signal] = 'd'
        eight = set(list(filter(lambda x: len(x)==7, signals))[0])
        bad_g_signal = list(filter(lambda x: x not in translator, eight))[0]
        translator[bad_g_signal] = 'g'
        # Convert output signal to digits
        output_values = all_output_values[idx]
        def translate(bad_signal):

            return signals_digit[''.join(sorted([translator[b] for b in bad_signal]))]
        numerical_output = 1000 * translate(output_values[0]) + \
                           100 * translate(output_values[1]) + \
                           10 * translate(output_values[2]) + \
                           translate(output_values[3])
        numerical_output_sum += numerical_output
    print(numerical_output_sum)



print("Example Two:")
two(example_input)

print("Real Two:")
two(input)
