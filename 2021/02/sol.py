input = open('input', 'r').read().strip()
input = [(lambda cmd, d: (cmd, int(d)))(*r.split()) for r in input.splitlines()]


def p1():
    x = y = 0
    for cmd, d in input:
        if cmd == 'up': y -= d
        if cmd == 'down': y += d
        if cmd == 'forward': x += d
    return x * y


def p2():
    x = y = aim = 0
    for cmd, d in input:
        if cmd == 'up': aim -= d
        if cmd == 'down': aim += d
        if cmd == 'forward': x += d; y += d * aim
    return x * y


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
