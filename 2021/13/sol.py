input = open('input', 'r').read().strip()
dots, folds = input.split('\n\n')
dots = [list(map(int, dot.split(','))) for dot in dots.splitlines()]
folds = [fold.split()[-1].split('=') for fold in folds.splitlines()]
folds = [(axis, int(coord)) for axis, coord in folds]


def fold_(dots, fold):
    axis, coord = fold
    new_dots = set()
    for x, y in dots:
        if axis == 'x' and x > coord: x = 2 * coord - x
        if axis == 'y' and y > coord: y = 2 * coord - y
        new_dots.add((x, y))
    return new_dots


def print_(paper):
    h, w = max(y for _, y in paper)+1, max(x for x, _ in paper)+1
    p = [[' '] * w for _ in range(h)]
    for x, y in paper: p[y][x] = '#'
    for r in p: print(*r, sep='')


def p1():
    return len(fold_(dots, folds[0]))


def p2():
    code = dots
    for fold in folds:
        code = fold_(code, fold)
    print_(code)


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
