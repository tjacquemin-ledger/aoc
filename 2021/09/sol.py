input = open('input', 'r').read().strip()
input = [list(map(int, r)) for r in input.splitlines()]

h, w = len(input), len(input[0])
in_ = [r + [10] for r in input] + [-~w * [10]]


def neighbours(point):
    x, y = point
    return {(x, y+1), (x, y-1), (x+1, y), (x-1, y)}


def low_points():
    return [(x, y) for x in range(h) for y in range(w)
            if all(in_[p][q] > in_[x][y] for p, q in neighbours((x, y)))]


def p1():
    return sum(in_[x][y]+1 for x, y in low_points())


def p2():
    def expand(point):
        basin, border = set(), {point}
        while border:
            basin |= border
            border = set().union(*map(neighbours, border))
            border = {(x, y) for x, y in border - basin if in_[x][y] < 9}
        return len(basin)

    return eval('*'.join(map(str, sorted(map(expand, low_points()))[-3:])))


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
