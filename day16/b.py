import sys

bins = []
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
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

ans = 0
def parse_packets(bins, num=None):
    global ans
    packets = []
    i = 0
    while i < len(bins):
        if len(bins) - i < 11:
            break
        # version and type id:
        version = int(''.join(bins[i:i+3]), 2)
        ans += version
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
                length = bins[i+1:i+12]
                i += 12
                data, l = parse_packets(bins[i:], length)
                i += l

        packets.append((version, typeid, data))
        if num and len(packets) == num:
            break
    if num:
        return packets, i
    return packets

packets = parse_packets(bins)
print(packets)
print(ans)