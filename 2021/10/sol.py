input = open('input', 'r').read().strip()
input = input.splitlines()

BRACKETS = "()[]{}<>"
BRACKETS = dict(zip(BRACKETS[::2], BRACKETS[1::2]))
POINTS = {
    **dict(zip(BRACKETS.values(), (3, 57, 1197, 25137))),
    **dict(zip(BRACKETS, (1, 2, 3, 4))),
}


def check(line):
    stack = [""]
    for c in line:
        if c in BRACKETS:
            stack.append(c)
        elif c != BRACKETS[stack.pop()]:
            return False, c
    return True, stack[1:]


def p1():
    return sum(POINTS[char] for correct, char in map(check, input) if not correct)


def p2():
    from functools import reduce
    from statistics import median
    return int(median(reduce(lambda x, c: 5 * x + POINTS[c], reversed(stack), 0)
                      for correct, stack in map(check, input) if correct))


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
