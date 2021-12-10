from collections import Counter
from math import gcd

input = open('input', 'r').read().strip()
input = [list(map(int, r.replace(' -> ', ',').split(','))) for r in input.splitlines()]


def lattice_points(with_diagonal):
    c = Counter()
    for x1, y1, x2, y2 in input:
        u, v = x2 - x1, y2 - y1
        if not with_diagonal and u and v: continue
        g = abs(gcd(u, v))
        for k in range(g+1):
            c[x1 + u // g * k, y1 + v // g * k] += 1
    return sum(v > 1 for v in c.values())


def p1():
    return lattice_points(False)


def p2():
    return lattice_points(True)


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
