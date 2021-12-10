input = open('input', 'r').read().strip()
input = list(map(int, input.splitlines()))


def p1(x=1):
    return sum(b > a for a, b in zip(input, input[x:]))


def p2():
    return p1(3)


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
