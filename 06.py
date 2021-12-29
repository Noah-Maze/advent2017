from aoc_util import *
from tqdm import tqdm

test()

raw_input = get_day(6)
raw_example_input = '''3,4,3,1,2'''

def process(input):
    return [int(i) for i in input.split(',')]

input = process(raw_input)
example_input = process(raw_example_input)

class Lanternfish:
    ''' each lanternfish creates a new lanternfish once every 7 days.

        a new lanternfish would surely need slightly longer before it's
        capable of producing more lanternfish:
            two more days for its first cycle.
    '''
    def __init__(self, days_to_spawn=8):
        self.days_to_spawn = days_to_spawn
        # print(f"Created new lanternfish that will spawn in {self.days_to_spawn} days.")
    def maybe_spawn(self):
        # print(f"Lanternfish will spawn in {self.days_to_spawn} days.")
        self.days_to_spawn -=1
        if self.days_to_spawn<0:
            self.days_to_spawn = 6
            return Lanternfish()
    def __str__(self):
        return f"<{self.days_to_spawn}><"

def test():
    fish = [Lanternfish(3)]
    for i in range(5):
        for f in fish:
            new_fish = f.maybe_spawn()
            if new_fish is not None:
                fish.append(new_fish)
test()

def one(input, days=80):
    fish = [Lanternfish(i) for i in input]
    for i in tqdm(range(days)):
        if days==18:
            print(' '.join(map(str, fish)))
        new_fish = []
        for f in fish:
            newest_fish = f.maybe_spawn()
            if newest_fish is not None:
                new_fish.append(newest_fish)
        fish.extend(new_fish)
    print(f"Total fish: {len(fish)}")

print("Example One:")
one(example_input, 18)
one(example_input)

print("Real One:")
one(input)

class LanternfishGeneration():
    def __init__(self, days_to_spawn=8, school_size=1):
        self.days_to_spawn = days_to_spawn
        self.school_size = school_size
        print(f"Created {self.school_size} lanternfish that will spawn in {self.days_to_spawn} days.")
    def maybe_spawn(self):
        # print(f"Lanternfish will spawn in {self.days_to_spawn} days.")
        self.days_to_spawn -=1
        if self.days_to_spawn<0:
            self.days_to_spawn = 6
            return LanternfishGeneration(8, self.school_size)
    def __str__(self):
        return f"{self.school_size}*<{self.days_to_spawn}><"

def two(input, days):
    def school(fish):
        # merge LanternfishGenerations with the same spawn date
        fish_generations = {}
        for f in fish:
            fish_generations[f.days_to_spawn] = fish_generations.get(f.days_to_spawn, 0) + f.school_size
        new_school = []
        for gen in fish_generations:
            size = fish_generations[gen]
            new_school.append(LanternfishGeneration(gen, size))
        return new_school
    fish = [LanternfishGeneration(i) for i in input]
    for i in tqdm(range(days)):
        print(' '.join(map(str, fish)))
        new_fish = []
        for f in fish:
            newest_fish = f.maybe_spawn()
            if newest_fish is not None:
                new_fish.append(newest_fish)
        fish.extend(new_fish)
        fish = school(fish)
    print(f"Total fish: {sum([f.school_size for f in fish])}")


print("Example Two:")
two(example_input, 256)

print("Real Two:")
two(input, 256)
