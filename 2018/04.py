from collections import Counter

# Input
with open('input/4', 'r') as f:
    unsorted_log = f.read().split('\n')

log = sorted(unsorted_log)

# Shifts begin when a guard signs on
shift_starts = [line_no for line_no in range(len(log)) if "Guard #" in log[line_no]]

print("\nExample shifts:")
print('\n'.join([log[shift] for shift in shift_starts[0:10]]))

print("\nExample full shift:")
print('\n'.join(log[shift_starts[0]:shift_starts[1]]))

guard_sleeps = {}

# For every shift, tally the total sleep time per guard
for shift_idx in range(len(shift_starts)):
    shift = shift_starts[shift_idx]
    if shift_idx+1<len(shift_starts):
        next_shift = shift_starts[shift_idx+1]
    else:
        next_shift = len(shift_starts)
    guard_id = log[shift][25:30]
    for sleep_line in range(shift+1, next_shift, 2):
        start_minute = int(log[sleep_line][15:17])
        stop_minute = int(log[sleep_line+1][15:17])
        sleep_minutes = stop_minute - start_minute
        guard_sleeps[guard_id] = sleep_minutes + guard_sleeps.get(guard_id, 0)

print("Sleepiest guard: ")
sleepiest_guard = max(guard_sleeps, key = lambda x: guard_sleeps[x])
print(sleepiest_guard)

sleepy_minutes_counter = Counter()
# For every shift of the sleepiest guard, tally the minutes
for shift_idx in range(len(shift_starts)):
    shift = shift_starts[shift_idx]
    if shift_idx+1<len(shift_starts):
        next_shift = shift_starts[shift_idx+1]
    else:
        next_shift = len(shift_starts)
    guard_id = log[shift][25:30]
    if guard_id!=sleepiest_guard:
        continue
    # make a list of minutes and feed 'em to a counter'
    for sleep_line in range(shift+1, next_shift, 2):
        start_minute = int(log[sleep_line][15:17])
        stop_minute = int(log[sleep_line+1][15:17])
        sleepy_minutes_counter.update(range(start_minute, stop_minute))

print("Sleepiest minute: ")
sleepiest_minute = sleepy_minutes_counter.most_common()[0][0]
print(sleepiest_minute)

answer = int(sleepiest_guard[1:])*sleepiest_minute
print("Answer: ", answer)

# Part 2
minute_counters_by_guard = {}
for shift_idx in range(len(shift_starts)):
    shift = shift_starts[shift_idx]
    if shift_idx+1<len(shift_starts):
        next_shift = shift_starts[shift_idx+1]
    else:
        next_shift = len(shift_starts)
    guard_id = log[shift][25:30]
    # make a list of minutes and feed 'em to a counter'
    for sleep_line in range(shift+1, next_shift, 2):
        start_minute = int(log[sleep_line][15:17])
        stop_minute = int(log[sleep_line+1][15:17])
        if guard_id in minute_counters_by_guard:
            minute_counters_by_guard[guard_id].update(range(start_minute, stop_minute))
        else:
            minute_counters_by_guard[guard_id]=Counter(range(start_minute, stop_minute))

best_guard = max(minute_counters_by_guard,
                 key=lambda x: minute_counters_by_guard[x].most_common()[0][1])
best_minute = minute_counters_by_guard[best_guard].most_common()[0][0]
print('''
Guard Id: {}
Minute: {}
Answer: {}
'''.format(best_guard, best_minute, int(best_guard[1:])*best_minute))
