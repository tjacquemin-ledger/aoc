from collections import Counter

input = open('input', 'r').read().strip()
template, input = input.split('\n\n')
input = [r.split(' -> ') for r in input.splitlines()]
table = {a+b: c for (a, b), c in input}


def p1(steps=10):
    # Bruteforce
    poly = template
    for _ in range(steps):
        poly = poly[0] + ''.join(table[a+b]+b for a, b in zip(poly, poly[1:]))
    c = Counter(poly)
    return max(c.values()) - min(c.values())


def p2(steps=40):
    poly = Counter([a+b for a, b in zip(template, template[1:])])
    for _ in range(steps):
        new_poly = Counter()
        for k, v in poly.items():
            for x in k[0] + table[k], table[k] + k[1]:
                new_poly[x] += v
        poly = new_poly
    c = Counter([template[0], template[-1]])
    for k, v in poly.items():
        for x in k: c[x] += v
    return (max(c.values()) - min(c.values())) // 2


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
