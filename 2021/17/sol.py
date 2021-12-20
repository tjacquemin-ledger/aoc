from re import findall
input = open('input', 'r').read().strip()
x_min, x_max, y_min, y_max = map(int, findall(r'-?\d+', input))


def tri(n):
    return n * -~n // 2


def tri_inv(x):
    return ~-int((8*x+1) ** .5) // 2


def p1():
    return tri(-y_min-1)


def p2():
    total = 0
    for vx0 in range(tri_inv(x_min), x_max + 1):
        for vy0 in range(y_min, -y_min + 1):
            x, y = 0, 0
            vx, vy = vx0, vy0
            while x <= x_max and y >= y_min:
                if x >= x_min and y <= y_max:
                    total += 1
                    break
                x, y = x+vx, y+vy
                vx, vy = max(0, vx-1), vy-1
    return total


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
