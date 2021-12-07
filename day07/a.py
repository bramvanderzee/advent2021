import sys

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

def fuel_use(pos, nums):
    total = 0
    for num in nums:
        total += abs(pos - num)
    return total

nums = []
with open(fn) as f:
    for l in f:
        nums = [int(n) for n in l.strip().split(',')]

average = round(sum(nums) / len(nums))

best_fuel = None
best_pos = 0
for pos in range(0, max(nums)):
    f = fuel_use(pos, nums)
    if not best_fuel:
        best_fuel = f
        best_pos = pos
    elif f < best_fuel:
        best_fuel = f
        best_pos = pos

print(best_fuel, best_pos)
