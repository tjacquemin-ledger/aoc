def cut(s):
    from itertools import islice
    try:
        it, b2n = iter(s), lambda b: int(''.join(next(it) for _ in range(b)), 2)
        version, type_id = b2n(3), b2n(3)
    except RuntimeError: return
    if type_id == 4:  # Literal
        read, bits = '1', []
        while read == '1':
            read, *chunks = (next(it) for _ in range(5))
            bits.extend(chunks)
        subs = int(''.join(bits), 2)
    else:  # Operator
        length_type = b2n(1)
        if length_type:  # Number
            subs = [cut(it) for _ in range(b2n(11))]
        else:  # Length
            subs, its = [], islice(s, b2n(15))
            while sub := cut(its): subs.append(sub)
    return version, type_id, subs


input = open('input', 'r').read().strip()
input = ''.join(f'{int(c, 16):04b}' for c in input)
input = cut(input)


def p1():
    def rec(packet):
        version, _, sub = packet
        if isinstance(sub, list): version += sum(map(rec, sub))
        return version
    return rec(input)


def p2():
    def rec(packet):
        from math import prod
        from operator import gt, lt, eq
        acc = [sum, prod, min, max, None, lambda x: gt(*x), lambda x: lt(*x), lambda x: eq(*x)]
        _, typ, sub = packet
        return reduce(map(rec, sub)) if (reduce := acc[typ]) else sub
    return rec(input)


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
