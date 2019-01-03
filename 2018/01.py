# Get Puzzle Input
IN_FILE = 'input/1'
INITIAL_FREQ = 0

frequency = INITIAL_FREQ
frequency_changes = []

for line in open(IN_FILE, 'r'):
    if len(line)>0:
        frequency_changes.append(int(line))
        frequency += int(line)

print('Final frequency: %s'%(frequency))

# Reset frequency and look for duplicate frequencies
frequency = INITIAL_FREQ
set_of_frequencies = set([INITIAL_FREQ])
freq_change_idx = 0
while(True):
    # Change frequency
    frequency+=frequency_changes[freq_change_idx]
    # Check if its in the set
    if frequency in set_of_frequencies:
        print('First repeated frequency: %s'%(frequency))
        break
    # Add it to the set
    set_of_frequencies.update([frequency])
    # Increment
    freq_change_idx = (freq_change_idx + 1)%len(frequency_changes)
