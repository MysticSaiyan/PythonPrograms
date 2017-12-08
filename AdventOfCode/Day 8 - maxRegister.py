#Cheated

from collections import defaultdict

f = open("Day8.txt").read().strip().splitlines()
regs = defaultdict(int)

def compute(left, op, right):
    try:
        left = int(left)
    except:
        left = regs[left]
    try:
        right = int(right)
    except:
        right = regs[right]
    return eval(str(left) + op + str(right))

m = 0
for line in f:
    reg, act, amt, _if, left, op, right = line.strip().split()
    if compute(left, op, right):
        if act == 'inc':
            asdf = int(amt)
        else:
            asdf = -int(amt)
        regs[reg] = regs[reg] + asdf
        m = max(regs[reg], m)

print(max(regs.values()))
print(m)