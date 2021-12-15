nums = []
width = None
with open('input.txt') as f:
    for l in f:
        num = l.strip()
        if not width:
            width = len(num)
        nums.append(num)

def calc_commons(nums):
    commons = [0 for _ in range(len(nums[0]))]
    for n in nums:
        for i,c in enumerate(n):
            commons[i] += 1 if c == '1' else -1
    return commons


oxygen = nums[:]
co = nums[:]
oxy_num = None
co_num = None
for index in range(width+1):
    if len(oxygen) == 1:
        oxy_num = oxygen[0]
    if len(co) == 1:
        co_num = co[0]
    if oxy_num and co_num:
        break
    
    if not oxy_num:
        most_common = '0' if calc_commons(oxygen)[index] < 0 else '1'
        oxygen = [n for n in oxygen if n[index] == most_common]
        
    if not co_num:
        least_common = '0' if calc_commons(co)[index] >= 0 else '1'
        co = [n for n in co if n[index] == least_common]
    
print(oxy_num, co_num)
print(int(oxy_num, 2),int(co_num, 2))
print(int(oxy_num, 2)*int(co_num, 2))