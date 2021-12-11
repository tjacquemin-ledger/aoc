input = open('input', 'r').read().strip()
input = [list(map(int, r)) for r in input.splitlines()]

h, w = len(input), len(input[0])


def neighbours(x, y):
    return [(p, q) for u in range(-1, 2) for v in range(-1, 2)
            if 0 <= (p := x+u) < h and 0 <= (q := y+v) < w]


def step(m):
    m = [[n+1 for n in r] for r in m]
    flashs, bag = set(), {(x, y) for x, r in enumerate(m) for y, n in enumerate(r) if n > 9}
    while bag:
        flashs |= bag
        expansion = set()
        for x, y in bag:
            for p, q in neighbours(x, y):
                if (p, q) in flashs: continue
                m[p][q] += 1
                expansion.add((p, q))
        bag = {(x, y) for x, y in expansion if m[x][y] > 9}
    for (x, y) in flashs: m[x][y] = 0
    return len(flashs), m


def p1(steps=100):
    s, m = 0, input
    for _ in range(steps):
        f, m = step(m)
        s += f
    return s


def p2():
    i, m = 0, input
    while 1:
        i += 1
        f, m = step(m)
        if f == h*w: return i


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
