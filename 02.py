from aoc_util import *
from collections import namedtuple

test()

# input is command, arg tuples
raw_in = get_day(2)
command_list = raw_in.split('\n')[0:-1]
State = namedtuple("State", "position, depth")
commands = {
    'forward': lambda state, arg: State(state.position+arg, state.depth),
    'down': lambda state, arg: State(state.position, state.depth+arg),
    'up': lambda state, arg: State(state.position, state.depth-arg),
    }

# One
def one(clist):
    current_state = State(0, 0)
    for command in clist:
        name, arg = command.split()
        current_state = commands[name](current_state, int(arg))
    print(current_state)
    print(f"Answer: {current_state.position*current_state.depth}")

one(command_list)

# Two
Rev2State = namedtuple("State", "position, depth, aim")
Rev2commands = {
    'forward': lambda state, arg: Rev2State(state.position+arg,
                                        state.depth+(state.aim*arg),
                                        state.aim),
    'down': lambda state, arg: Rev2State(state.position,
                                     state.depth,
                                     state.aim+arg),
    'up': lambda state, arg: Rev2State(state.position,
                                     state.depth,
                                     state.aim-arg),
    }
def two(clist):
    current_state = Rev2State(0, 0, 0)
    for command in clist:
        name, arg = command.split()
        current_state = Rev2commands[name](current_state, int(arg))
    print(current_state)
    print(f"Answer: {current_state.position*current_state.depth}")

two(command_list)
