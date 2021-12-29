from aoc_util import *

from collections import Counter

test()

raw_input = get_day(5).split('\n')
example_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''.split('\n')

class Line:
    def __init__(self, def_str):
        # Def str looks like 0,9 -> 5,9
        (start, end) = def_str.split(' -> ')
        self.def_str = def_str
        start_strs = start.split(',')
        self.start = (int(start_strs[0]), int(start_strs[1]))
        end_strs = end.split(',')
        self.end = (int(end_strs[0]), int(end_strs[1]))
    def __str__(self):
        return f"Line [{self.def_str}] (Points: {self.points()})"
    def __repr__(self):
        return self.__str__()
    def is_flat(self):
        return self.start[0]==self.end[0] or self.start[1]==self.end[1]
    def points(self):
        def halfway_point_or_points(s, e):
            midpoint = ( (s[0]+e[0])/2.0, (s[1]+e[1])/2.0 )
            if midpoint[1]%1==0.5 and midpoint[0]%1==0.5:
                # Round towards start
                first_point = (
                    ifloor(midpoint[0]) if midpoint[0]>s[0] else iceil(midpoint[0]),
                    ifloor(midpoint[1]) if midpoint[1]>s[1] else iceil(midpoint[1])
                )
                # Round towards end
                second_point = (
                    ifloor(midpoint[0]) if midpoint[0]>e[0] else iceil(midpoint[0]),
                    ifloor(midpoint[1]) if midpoint[1]>e[1] else iceil(midpoint[1])
                )
                return [first_point, second_point]
            if midpoint[0]%1==0.5:
                return [(ifloor(midpoint[0]), int(midpoint[1])), (iceil(midpoint[0]), int(midpoint[1]))]
            if midpoint[1]%1==0.5:
                return [(int(midpoint[0]), ifloor(midpoint[1])), (int(midpoint[0]), iceil(midpoint[1]))]
            return [(int(midpoint[0]), int(midpoint[1]))]
        last_points = []
        next_points = [self.start, self.end]
        while (set(last_points)!=set(next_points)):
            # print(f"{last_points} => {next_points}")
            last_points = next_points
            next_points = []
            for point_no in range(len(last_points)-1):
                start = last_points[point_no]
                end = last_points[point_no+1]
                next_points.append(start)
                next_points.extend(halfway_point_or_points(start, end))
            next_points.append(end)
        # print(f"Finally, {last_points} => {next_points}")
        return list(set(last_points))

def one(input):
    lines = [Line(line_str) for line_str in input[:-1]]
    # print('\n'.join(str(l) for l in lines))
    flat_lines = filter(lambda x: x.is_flat(), lines)
    points = []
    for fline in flat_lines:
        points.extend(fline.points())
    point_counter = Counter(points)
    overlap_points = list(filter(lambda x: point_counter[x]>1, point_counter))
    print(f"{len(overlap_points)} points overlap")

print("Example One:")
one(example_input)

print("Real One:")
one(raw_input)

def two(input):
      lines = [Line(line_str) for line_str in input[:-1]]
      # print('\n'.join(str(l) for l in lines))
      points = []
      for line in lines:
          points.extend(line.points())
      point_counter = Counter(points)
      overlap_points = list(filter(lambda x: point_counter[x]>1, point_counter))
      print(f"{len(overlap_points)} points overlap including nonflat lines")

print("Example Two:")
two(example_input)

print("Real Two:")
two(raw_input)
