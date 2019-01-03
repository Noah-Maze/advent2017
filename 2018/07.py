from pprint import pprint

def parse_line(line):
    parent = line[5:6]
    child = line[36:37]
    return parent, child

# key: parents
tree = {}

with open('input/7', 'r') as f:
    for line in f:
        parent, child = parse_line(line)
        tree[child] = tree.get(child, [])+[parent]
        if parent not in tree:
            tree[parent] = []

pprint(tree)

output = []
while len(output)<len(tree):
    for k in sorted(tree.keys()):
        # Continue if we've already done it
        if k in output:
            continue
        # Continue if the parents aren't done
        missing_parents = 0
        for parent in tree[k]:
            if parent not in output:
                missing_parents+=1
        # If we get here it's safe to do this task
        if missing_parents==0:
            output.append(k)
            break
    print(''.join(output))

# Work in queue
work_by_worker = [None] * 5

def task_time(ch):
    return ord(ch)-4

def next_task(tree, output):
    output = []
    while len(output)<len(tree):
        for k in sorted(tree.keys()):
            # Continue if we've already done it
            if k in output:
                continue
            # Continue if the parents aren't done
            missing_parents = 0
            for parent in tree[k]:
                if parent not in output:
                    missing_parents+=1
            # If we get here it's safe to do this task
            if missing_parents==0:
                output.append(k)
                break
        print(''.join(output))

Resources:
A directed graph
Task times

Track workers as (T, start_time)
workers = [(None, None)]*5
for sec in range((60+26)*26):
    # update workers who finished their tasks
    for task, start_time in old_work:
         = w

    #
