

def manhattan_sp(desired_cell):
    ''' Return the manhattan distance
        from Cell Number 1 for a
        given cell in a spiral
        arranged like so:

            17  16  15  14  13
            18   5   4   3  12
            19   6   1   2  11
            20   7   8   9  10
            21  22  23---> ...

        For example:
            # manhattan_sp(1) = 0, since Cell 1 is 0 cells away from itself.
            # manhattan_sp(12) = 3, because it is two cells 'left' and one
                cell 'up' from Cell 1
            # manhattan_sp(23) = 2, because it is two cells below Cell 1
            # manhattan_sp(1024) = 31
    '''
    def rotate(heading):
        ''' Rotate the heading 90 degrees CCW
        '''
        return (-heading[1], heading[0])
    def hallways():
        ''' The Spiral's hallways have a nice rhythm!
            Starting at Cell 1, move:
                East 1
                North 1
                West 2
                South 2
                East 3
                North 3
                etc
            The direction is tracked by the called so
            this generator just spits out integers like
            1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
        '''
        i = 1
        while True:
            yield i
            yield i
            i+=1
    # Start at Cell 1
    cell_number = 1
    x = 0
    y = 0
    # Facing East
    heading = (1,0)
    # Walk down longer and longer hallways
    for hall in hallways():
        for cell in range(hall):
            if cell_number == desired_cell:
                # Return the manhattan distance from Cell 1
                return abs(x) + abs(y)
            # Move in the direction of heading to the next cell
            x += heading[0]
            y += heading[1]
            cell_number +=1
        # Turn left at the end of the hallway
        heading = rotate(heading)

# tests
assert manhattan_sp(1)==0
assert manhattan_sp(12)==3
assert manhattan_sp(23)==2
assert manhattan_sp(1024)==31

print "Answer for Part One: " + str(manhattan_sp(289326))

def weird_mem(max_value):
    def rotate(heading):
        return (-heading[1], heading[0])
    def hallways():
        i = 1
        while True:
            yield i
            yield i
            i+=1
    # keep track of written cells
    cells = {(0,0):1} # Special case for 1st cell
    value = 1
    idx = 1
    x = 0
    y = 0
    heading = (1,0)
    for hall in hallways():
        for cell in range(hall):
            if value >= max_value:
                return value
            x += heading[0]
            y += heading[1]
            value =(cells.get((x-1, y+1), 0) + cells.get((x+0, y+1), 0) + cells.get((x+1, y+1), 0) +
                    cells.get((x-1, y+0), 0) + cells.get((x,y), 0)      + cells.get((x+1, y+0), 0) +
                    cells.get((x-1, y-1), 0) + cells.get((x+0, y-1), 0) + cells.get((x+1, y-1), 0))
            cells[(x,y)]=value
            # Potential Optimization: Forget cells that are useless (if ram usage explodes)
            idx +=1
        heading = rotate(heading)

print "Answer for Part Two: " + str(weird_mem(289326))
