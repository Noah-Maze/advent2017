def jump_and_increment(position, state):
    if len(state)<(position+1):
        print "We're off the board!!!"
        return None
    state[position]+=1
    position+=(state[position]-1)
    return position, state

def show(position, state):
    line = ''
    for idx in range(len(state)):
        if idx==position:
            line += '(%s)\t'%(state[idx])
        else:
            line += '%s\t'%(state[idx])
    print line

# Test
position = 0
jumps = 0
state = [0, 3,  0,  1,  -3]
while (position+1)<=len(state):
    show(position, state)
    position, state = jump_and_increment(position, state)
    jumps+=1

print(jumps)

# Real
position = 0
jumps = 0

state = []
with open('long_inputs/05','r') as f:
    for line in f:
        state.append(int(line.strip()))

print state

while (position+1)<=len(state):
    position, state = jump_and_increment(position, state)
    jumps+=1

print(jumps)

# Two
def new_jump_and_increment(position, state):
    if len(state)<(position+1):
        print "We're off the board!!!"
        return None
    jump_dist = state[position]
    if jump_dist >= 3:
        state[position]-=1
    else:
        state[position]+=1
    position+=(jump_dist)
    return position, state

position = 0
jumps = 0
state = []
with open('long_inputs/05','r') as f:
    for line in f:
        state.append(int(line.strip()))

while (position+1)<=len(state):
    position, state = new_jump_and_increment(position, state)
    jumps+=1

print jumps
