input = open('input', 'r').read().strip()
input = [list(map(int, r)) for r in input.splitlines()]


def neighbours(x, y, h, w):
    return {(p, q) for u, v in ((1, 0), (0, -1), (-1, 0), (0, 1))
            if 0 <= (p := x+u) < h and 0 <= (q := y+v) < w}


def p1():
    m = input
    # Dict based
    seen, bag = set(), {(0, 0): 0}
    while bag:
        x, y = min(bag, key=bag.get)
        risk = bag.pop((x, y))
        seen.add((x, y))
        if (x, y) == (len(m)-1, len(m[0])-1): return risk
        for p, q in neighbours(x, y, len(m), len(m[0])):
            if (p, q) in seen or risk + m[p][q] >= bag.get((p, q), float('inf')): continue
            bag[p, q] = risk + m[p][q]


def p2():
    m = [[(n+u+v-1) % 9 + 1 for v in range(5) for n in r] for u in range(5) for r in input]
    # Heap based
    from heapq import heappush, heappop
    mins, bag = {(0, 0): 0}, [(0, (0, 0))]
    while bag:
        risk, (x, y) = heappop(bag)
        if (x, y) == (len(m)-1, len(m[0])-1): return risk
        for p, q in neighbours(x, y, len(m), len(m[0])):
            if risk + m[p][q] < mins.get((p, q), float('inf')):
                mins[p, q] = risk + m[p][q]
                heappush(bag, (risk + m[p][q], (p, q)))


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
