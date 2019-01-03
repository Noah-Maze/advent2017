with open('input/6', 'r') as f:
    nodes = [tuple(map(int,x.split(', '))) for x in  f.read().split('\n') if ',' in x]

y_min = None
y_max = None
x_min = None
x_max = None

for node in nodes:
    if y_min:
        y_min=min([y_min, node[1]])
    else:
        y_min = node[1]
    if y_max:
        y_max=max([y_max, node[1]])
    else:
        y_max = node[1]
    if x_min:
        x_min=min([x_min, node[0]])
    else:
        x_min = node[0]
    if x_max:
        x_max=max([x_max, node[0]])
    else:
        x_max = node[0]

node_domain_sizes = [0]*len(nodes)

def node_distance(x, y, nx, ny):
    return abs(nx-x)+abs(y-ny)

for x_t in range(x_min, x_max+1):
    for y_t in range(y_min, y_max+1):
        # Get nearest tiles
        closest_tiles = sorted(nodes, key=lambda n: node_distance(x_t, y_t, n[0], n[1]))[0:2]
        # If there's a tie for the lead it doesn't count for anything
        if (node_distance(x_t, y_t, closest_tiles[0][0], closest_tiles[0][1])==\
            node_distance(x_t, y_t, closest_tiles[1][0], closest_tiles[1][1])):
            continue
        king_node = nodes.index(closest_tiles[0])
        # If it is an edge piece set the node domain size to None
        if (x_t==x_min or
            x_t==x_max or
            y_t==x_max or
            y_t==x_min):
            node_domain_sizes[king_node]=None
        # If its size isn't None then count it
        if node_domain_sizes[king_node] is not None:
            node_domain_sizes[king_node]+=1

print("Biggest Area: ", max(node_domain_sizes, key=lambda x: x if x is not None else -1))

# Part two
D_MAX = 10000

def close_enough(x,y,nodes, max=D_MAX):
    aggregate_distance = 0
    for node in nodes:
        aggregate_distance += abs(node[0]-x)+abs(y-node[1])
        if aggregate_distance>=max:
            return False
    return True

close_enough_area = 0
max_possible_distance = int(D_MAX/len(nodes))
for x_t in range(x_min-max_possible_distance, x_max+1+max_possible_distance):
    for y_t in range(y_min-max_possible_distance, y_max+1+max_possible_distance):
        if close_enough(x_t, y_t, nodes):
            close_enough_area+=1

print("Size of the Safe Zone: ", close_enough_area)
