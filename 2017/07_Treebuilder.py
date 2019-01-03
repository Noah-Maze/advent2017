from collections import Counter

test_tree_file = 'long_inputs/07_test'
tree_file = 'long_inputs/07'

def rebuild_tree(infile):
    parent = {}
    children = {}
    weight = {}
    with open(infile, 'r') as f:
        for line in f:
            row = line.strip().split()
            # Row is like ['fwft', '(72)', '->', 'ktlj,', 'cntj,', 'xhth']
            weight[row[0]]=int(row[1][1:-1])
            if len(row)>3:
                for child in row[3:]:
                    child_name = child
                    if child[-1]==',':
                        child_name = child[:-1]
                    children[row[0]] = children.get(row[0], []) + [child_name]
                    parent[child_name] = row[0]
    node_set = set(weight.keys())
    child_set = set(parent.keys())
    print "Parent Node: " + str(list(node_set - child_set)[0])
    return parent, children, weight

test_parent, test_children, test_weight = rebuild_tree(test_tree_file)
parent, children, weight = rebuild_tree(tree_file)

def get_combined_weight(node_name, parent, children, weight):
    family = children.get(node_name, None)
    my_weight = weight[node_name]
    if family:
        for child in family:
            my_weight+=get_combined_weight(child, parent, children, weight)
    return my_weight

# for each group of kids
def print_bad_siblings(parent, children, weight):
    for kids in children.values():
        kid_combined_weights = [get_combined_weight(kid, parent, children, weight) for kid in kids]
        ranked_weight_counts = Counter(kid_combined_weights).most_common()
        if len(ranked_weight_counts)>1:
            print "Found an unbalanced family!"
            print kids
            print kid_combined_weights
            bad_kid = kids[kid_combined_weights.index(ranked_weight_counts[-1][0])]
            print bad_kid + ' is the bad kid'
            print "Original weight: "
            print weight[bad_kid]
            print "Suggested weight: "
            print weight[bad_kid]-(ranked_weight_counts[-1][0]-ranked_weight_counts[0][0])

print_bad_siblings(test_parent, test_children, test_weight)
