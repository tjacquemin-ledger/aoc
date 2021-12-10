from collections import Counter

input = open('input', 'r').read().strip()
input = input.splitlines()


def p1():
    def filter(f):
        return int(''.join(f(c := Counter(col), key=c.get) for col in zip(*input)), 2)

    return filter(min) * filter(max)


def p2():
    def filter(f):
        bag = input
        for i, _ in enumerate(zip(*input)):
            criteria = f(c := Counter(b[i] for b in bag), key=lambda k: (c[k], k))
            bag = [b for b in bag if b[i] == criteria]
            if len(bag) == 1: return int(bag.pop(), 2)

    return filter(min) * filter(max)


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
