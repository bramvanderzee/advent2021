import sys

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

DP = {}
def fuel_use(pos, nums):
    total = 0
    for num in nums:
        diff = abs(pos - num)
        if diff not in DP.keys():
            DP[diff] = sum(range(1, diff+1))
        total += DP[diff]
    return total

nums = []
with open(fn) as f:
    for l in f:
        nums = [int(n) for n in l.strip().split(',')]

average = round(sum(nums) / len(nums))

best_fuel = 1e9
best_pos = 0
for pos in range(0, max(nums)):
    f = fuel_use(pos, nums)
    if f < best_fuel:
        best_fuel = f
        best_pos = pos

print(best_fuel, best_pos)
