
# Constants to make state machine more readable
DEFAULT = 1
GARBAGE = 2
CANCELLED= 3

def parsed_stream(stream):
    ''' Outputs stream groups in (score, contents) tuples
    '''
    state = DEFAULT
    previous_state = DEFAULT
    # h/t to https://stackoverflow.com/a/4285211
    # for the stack idea
    stack = []
    garbage_characters = 0
    for i, c in enumerate(stream):
        if state is DEFAULT:
            if c == '{':
                stack.append(i)
            elif c == '}' and stack:
                start = stack.pop()
                yield (len(stack)+1, stream[start + 1: i])
            elif c == '<':
                state = GARBAGE
            elif c=='!':
                previous_state = DEFAULT
                state = CANCELLED
        elif state is GARBAGE:
            if c=='!':
                previous_state = GARBAGE
                state = CANCELLED
            elif c=='>':
                state = DEFAULT
            else:
                garbage_characters+=1
        elif state is CANCELLED:
            state = previous_state
    print "Found %s garbage characters"%(garbage_characters)

def stream_score(stream):
    score = 0
    for group in parsed_stream(stream):
        score += group[0]
    return score

assert stream_score('{}')==1
assert stream_score('{{{}}}')==6
assert stream_score('{{},{}}')==5
assert stream_score('{{{},{},{{}}}}')==16
assert stream_score('{<a>,<a>,<a>,<a>}')==1
assert stream_score('{{<ab>},{<ab>},{<ab>},{<ab>}}')==9
assert stream_score('{{<!!>},{<!!>},{<!!>},{<!!>}}')==9
assert stream_score('{{<a!>},{<a!>},{<a!>},{<ab>}}')==3

real_stream = open('long_inputs/09','r').read()

print "Part One: " + str(stream_score(real_stream))
