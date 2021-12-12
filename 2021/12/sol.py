input = open('input', 'r').read().strip()
graph = {}
for edge in input.splitlines():
    a, b = edge.split('-')
    if not (a == 'end' or b == 'start'): graph.setdefault(a, set()).add(b)
    if not (a == 'start' or b == 'end'): graph.setdefault(b, set()).add(a)


def p1():
    paths, bag = 0, [('start', set())]
    while bag:
        source, seen = bag.pop()
        if source.islower(): seen.add(source)
        if source == 'end':
            paths += 1
            continue
        for target in graph[source]:
            if target not in seen:
                bag.append((target, seen.copy()))
    return paths


def p2():
    paths, bag = 0, [('start', set(), False)]
    while bag:
        source, seen, twice = bag.pop()
        if source.islower():
            if source in seen: twice = True
            else: seen.add(source)
        if source == 'end':
            paths += 1
            continue
        for target in graph[source]:
            if not (target in seen and twice):
                bag.append((target, seen.copy(), twice))
    return paths


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
