from math import floor, ceil
from statistics import mean, median

input = open('input', 'r').read().strip()
input = list(map(int, input.split(',')))


def p1():
    # Bruteforce
    # return min(sum(abs(x-y) for y in input) for x in range(max(input)))
    # Linear
    m = int(median(input))
    return sum(abs(x-m) for x in input)


def p2():
    # Bruteforce
    # return min(sum((n := abs(x-y)) * -~n // 2 for y in input) for x in range(max(input)))
    # Linear
    m = mean(input)
    return min(sum((n := abs(x-f(m))) * -~n // 2 for x in input) for f in (ceil, floor))


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
