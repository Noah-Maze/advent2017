from collections import Counter

# Get Puzzle Input
IN_FILE = 'input/2'

test_list = ['abcdef',
             'bababc',
             'abbcde',
             'abcccd',
             'aabcdd',
             'abcdee',
             'ababab']

def checkbox(boxlist):
    doubles = 0
    triples = 0
    for box in boxlist:
        letter_counts = Counter(box)
        if 2 in letter_counts.values():
            doubles+=1
        if 3 in letter_counts.values():
            triples+=1
    return doubles * triples

print('Test Result: ' + str(checkbox(test_list)))

with open(IN_FILE, 'r') as f:
    boxlist = f.read().split()

print("Real Result: " + str(checkbox(boxlist)))

for box_no in range(len(boxlist)):
    for neighbor_no in range(box_no+1, len(boxlist)):
        this_box = boxlist[box_no]
        that_box = boxlist[neighbor_no]
        score=0
        common_letters = ''
        if len(this_box)==len(that_box):
            for idx in range(len(this_box)):
                if this_box[idx]==that_box[idx]:
                    score+=1
                    common_letters+=this_box[idx]
        if score==len(this_box)-1:
            print('Found a matched pair! Matching letters: %s'%(common_letters))
            break
