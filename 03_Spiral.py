
def man(max_idx):
    def rotate(heading):
        if heading==(1,0):
            return (0,1)
        if heading==(0,1):
            return (-1,0)
        if heading==(-1,0):
            return (0,-1)
        if heading==(0,-1):
            return (1,0)
    def hallways():
        i = 1
        while True:
            yield i
            yield i
            i+=1
    idx = 1
    x = 0
    y = 0
    heading = (1,0)
    for hall in hallways():
        for cell in range(hall):
            if idx == max_idx:
                return abs(x) + abs(y)
            x += heading[0]
            y += heading[1]
            idx +=1
        heading = rotate(heading)

# tests
    # Data from square 1 is carried 0 steps, since it's at the access port.
    # Data from square 12 is carried 3 steps, such as: down, left, left.
    # Data from square 23 is carried only 2 steps: up twice.
    # Data from square 1024 must be carried 31 steps.
assert man(1)==0
assert man(12)==3
assert man(23)==2
assert man(1024)==31

print(man(289326))

def weird_ram(max_idx, max_value):
    def rotate(heading):
        if heading==(1,0):
            return (0,1)
        if heading==(0,1):
            return (-1,0)
        if heading==(-1,0):
            return (0,-1)
        if heading==(0,-1):
            return (1,0)
    def hallways():
        i = 1
        while True:
            yield i
            yield i
            i+=1
    # keep track of written cells until they're useless
    outer_cells = {(0,0):1} # Special case for 1st idx
    value = 1
    idx = 1
    x = 0
    y = 0
    heading = (1,0)
    for hall in hallways():
        for cell in range(hall):
            print ((x, y), value)
            if value >= max_value or idx > max_idx:
                return value
            x += heading[0]
            y += heading[1]
            value =(outer_cells.get((x-1, y+1), 0) + outer_cells.get((x+0, y+1), 0) + outer_cells.get((x+1, y+1), 0) +
                    outer_cells.get((x-1, y+0), 0) + outer_cells.get((x,y), 0)      + outer_cells.get((x+1, y+0), 0) +
                    outer_cells.get((x-1, y-1), 0) + outer_cells.get((x+0, y-1), 0) + outer_cells.get((x+1, y-1), 0))
            outer_cells[(x,y)]=value
            # TODO: Pop cells that are useless if ram usage explodes
            idx +=1
        heading = rotate(heading)
