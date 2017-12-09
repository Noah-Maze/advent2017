from collections import defaultdict

class Instruction(object):
    def __init__(self, line):
        row = line.strip().split()
        self.target = row[0]
        self.delta = int(row[2]) if row[1]=='inc' else int(row[2])*-1
        self.condition_str = "d['"+row[4]+"']"+row[5]+row[6]
    def condition(self, d):
        return eval(self.condition_str)

def process_instructions(instruction_file):
    registers = defaultdict(lambda : 0)
    with open(instruction_file, 'r') as f:
        for line in f:
            inst = Instruction(line)
            if inst.condition(registers):
                registers[inst.target]+=inst.delta
    return registers

# Test
test_registers = process_instructions('long_inputs/08_test')
assert max(test_registers.values())==1

registers = process_instructions('long_inputs/08')
print "Part One Answer: " + str(max(registers.values()))

# Part Two
def process_instructions_and_track_max(instruction_file):
    registers = defaultdict(lambda : 0)
    highest_value_ever = 0
    with open(instruction_file, 'r') as f:
        for line in f:
            inst = Instruction(line)
            if inst.condition(registers):
                registers[inst.target]+=inst.delta
                highest_value_ever = max([registers[inst.target], highest_value_ever])
    print "Part Two Answer: " + str(highest_value_ever)
    return registers

registers = process_instructions_and_track_max('long_inputs/08')
