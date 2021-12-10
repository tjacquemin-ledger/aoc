from collections import deque

input = open('input', 'r').read().strip()
input = list(map(int, open('input', 'r').read().split(',')))


def p1(days=80):
    count = [0] * 9
    for x in input: count[x] += 1
    q = deque(count)
    for _ in range(days):
        p = q.popleft()
        q.append(p)
        q[6] += p
    return sum(q)


def p2(days=256):
    return p1(days)


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
