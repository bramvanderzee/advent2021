import sys

bins = []
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
if len(sys.argv) > 2:
    for c in sys.argv[2]:
        bins.extend(str(bin(int(c, 16)))[2:].zfill(4))
else:
    with open(fn) as f:
        for l in f:
            for c in l.strip():
                bins.extend(str(bin(int(c, 16)))[2:].zfill(4))

def type_4(bins, i):
    groups = []
    last = False
    while not last:
        group = bins[i:i+5]
        groups.extend(group[1:])
        i += 5
        if group[0] == '0':
            break
    return int(''.join(groups), 2), i

def parse_packets(bins, num=None):
    packets = []
    i = 0
    while i < len(bins):
        if len(bins) - i < 11:
            break
        # version and type id:
        version = int(''.join(bins[i:i+3]), 2)
        typeid = int(''.join(bins[i+3:i+6]), 2)
        i += 6
        data = []
        if typeid == 4:
            data, i = type_4(bins, i)
        else:
            if bins[i] == '0':
                length = int(''.join(bins[i+1:i+16]), 2)
                i += 16
                data = parse_packets(bins[i:i+length])
                i += length
            else:
                length = int(''.join(bins[i+1:i+12]), 2)
                i += 12
                data, l = parse_packets(bins[i:], length)
                i += l

        packets.append((version, typeid, data))
        if num and len(packets) == num:
            break
    if num:
        return packets, i
    return packets

def get_data(packet):
    v, t, d = packet
    if type(d) != int:
        return evaluate([packet])
    return d

# Type IDs:
# 0: sum
# 1: product
# 2: minimum
# 3: maximum
# 4: literal value
# 5: greater than
# 6: less than
# 7: equal to
def evaluate(packets):
    ret = 0
    for p in packets:
        ans = 0
        version, typeid, data = p
        if typeid == 0:
            print('+', data)
            for d in data:
                ans += get_data(d)
        elif typeid == 1:
            print('*', data)
            ans = 1
            for d in data:
                ans *= get_data(d)
        elif typeid == 2:
            print('min', data)
            l = []
            for d in data:
                l.append(get_data(d))
            ans = min(l)
        elif typeid == 3:
            print('max', data)
            l = []
            for d in data:
                l.append(get_data(d))
            ans = max(l)
        elif typeid == 4:
            print('l', data)
            ans = data
        elif typeid == 5:
            print('>', data)
            a = []
            for d in data:
                a.append(get_data(d))
            ans = int(a[0] > a[1])
        elif typeid == 6:
            print('<', data)
            a = []
            for d in data:
                a.append(get_data(d))
            ans = int(a[0] < a[1])
        elif typeid == 7:
            print('=', data)
            a = []
            for d in data:
                a.append(get_data(d))
            ans = int(a[0] == a[1])
        print(ans)
        ret += ans
    return ret

packets = parse_packets(bins)
print(evaluate(packets))