# Input
with open('input/5', 'r') as f:
    polymer = f.read().strip()

print("Initial polymer length: ", len(polymer))

def react(polymer, debug=True):
    if debug:
        print(polymer)
    for c_idx in range(len(polymer)-1):
        if ((polymer[c_idx].isupper() and
             polymer[c_idx].lower()==polymer[c_idx+1]) or
            (polymer[c_idx+1].isupper() and
             polymer[c_idx+1].lower()==polymer[c_idx])):
             polymer = polymer[0:c_idx] + "##" + polymer[c_idx+2:]
    return polymer.replace('#','')

def completely_reduce(polymer):
    old_polymer = None
    while(polymer!=old_polymer):
        old_polymer = polymer
        polymer = react(polymer, False)
    return polymer

reduced_polymer = completely_reduce(polymer)
print("Final polymer length: ", len(reduced_polymer))

def cleansed_polymer_length(bad_unit):
    cleansed_polymer = polymer.replace(bad_unit, '').replace(bad_unit.upper(), '')
    reduced_cleansed_polymer = completely_reduce(cleansed_polymer)
    return len(reduced_cleansed_polymer)

units = list(set(polymer.lower()))
worst_unit = min(units, key=cleansed_polymer_length)
print("Worst unit: ", worst_unit)
print("Length: ", cleansed_polymer_length(worst_unit))
