from aoc_util import *

from pprint import pprint as p
from collections import Counter
from statistics import median

test()

raw_input = get_day(10)
raw_example_input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''

def process(input):
    return input.split('\n')[:-1]

input = process(raw_input)
example_input = process(raw_example_input)

test()

def flip(brac):
    bracket_pairs = {
        '[':']',
        ']':'[',
        '{':'}',
        '}':'{',
        '(':')',
        ')':'(',
        '<':'>',
        '>':'<'
    }
    return bracket_pairs[brac]

scores = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

openers = '[{(<'

def one(input):
    syntax_error_score = 0
    for line in input:
        brac_stack = ''
        for brac in line:
            if brac in openers:
                brac_stack += brac
            else:
                if brac_stack[-1]==flip(brac):
                    brac_stack = brac_stack[:-1]
                else:
                    print(f"Bracket error!  Expected opener or {flip(brac_stack[-1])}, but got {brac}")
                    syntax_error_score += scores[brac]
                    break
        if len(brac_stack)>0:
            print(f"Incomplete line.  Unclosed brackets: {brac_stack}")
    print(f"Final Syntax Error Score: {syntax_error_score}")

print("Example One:")
one(example_input)

print("Real One:")
one(input)

fix_scores = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

def two(input):
    scores = []
    for line in input:
        line_score = 0
        line_is_bad = False
        brac_stack = ''
        for brac in line:
            if brac in openers:
                brac_stack += brac
            else:
                if brac_stack[-1]==flip(brac):
                    brac_stack = brac_stack[:-1]
                else:
                    print(f"Bracket error!  Expected opener or {flip(brac_stack[-1])}, but got {brac}")
                    line_is_bad = True
                    break
        if line_is_bad:
            continue
        if len(brac_stack)>0:
            print(f"Incomplete line.  Unclosed brackets: {brac_stack}")
            for brac in reversed(brac_stack):
                line_score *= 5
                line_score += fix_scores[flip(brac)]
            print(f"  Fixed!  Fix Score: {line_score}")
            scores.append(line_score)
    print(f"Median Fix Score: {median(sorted(scores))}")

print("Example Two:")
two(example_input)

print("Real Two:")
two(input)
