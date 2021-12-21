from functools import reduce
from itertools import permutations


def flatten(row):
    depth, flat = -1, []
    for c in row:
        if c == '[': depth += 1
        if c == ']': depth -= 1
        if c.isdigit(): flat.append([depth, int(c)])
    return flat


input = open('input', 'r').read().strip()
input = list(map(flatten, input.splitlines()))


def explode(x):
    for i, ((d0, n0), (d1, n1)) in enumerate(zip(x, x[1:])):
        if d0 == d1 >= 4:
            if i > 0: x[i-1][1] += n0
            if i < len(x)-2: x[i+2][1] += n1
            x[i: i+2] = [[d0-1, 0]]
            return True


def split(x):
    for i, (depth, n) in enumerate(x):
        if n >= 10:
            x[i: i+1] = [[depth+1, n // 2], [depth+1, -~n // 2]]
            return True


def add(a, b):
    x = [[depth+1, n] for depth, n in a + b]
    while explode(x) or split(x): continue
    return x


def magnitude(x):
    while len(x) > 1:
        for i, ((d0, n0), (d1, n1)) in enumerate(zip(x, x[1:])):
            if d0 == d1:
                x[i: i+2] = [[d0-1, 3*n0 + 2*n1]]
                break
    return x[0][1]


def p1():
    return magnitude(reduce(add, input))


def p2():
    return max(magnitude(add(a, b)) for a, b in permutations(input, r=2))


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)

