

test_banks = [0, 2, 7, 0]

def loop_length(banks, verbose=False):
    result = banks
    previous_states = []
    length = 0
    if verbose:
        print '\t'.join(map(str, range(len(banks))))
    while True:
        # find biggest bank
        big_bank_idx = result.index(max(result))
        big_bank_value = result[big_bank_idx]
        if verbose:
            print '\t'.join(map(str, result)) + " -- Biggest bank is Bank %s after %s redistributions."%(big_bank_idx, length)
        # redistribute
        result[big_bank_idx]=0
        for item in range(big_bank_value):
            result[(big_bank_idx+1+item)%len(banks)]+=1
        length +=1
        # bail if it's a repeat
        if tuple(result) in previous_states:
            if verbose:
                print '\t'.join(map(str, result)) + " -- Found loop after redistribution %s."%(length)
            return length, len(previous_states)-previous_states.index(tuple(result))
        # store current state
        previous_states.append(tuple(result))

loop_length(test_banks, verbose=True)


advent_banks = [int(x) for x in '4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3'.split()]
loop_length(advent_banks, verbose=False)
