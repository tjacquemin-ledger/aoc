from copy import deepcopy

input = open('input', 'r').read().strip()

numbers, *boards = input.split('\n\n')
numbers = list(map(int, numbers.split(',')))
boards = [[list(map(int, r.split())) for r in b.splitlines()] for b in boards]


def mark(b, n):
    try:
        i, j = next((i, j) for i, r in enumerate(b) for j, m in enumerate(r) if m == n)
        b[i][j] = None
        return b
    except StopIteration: pass


def win(s):
    return any(all(x is None for x in r) for r in s + list(zip(*s)))


def score(b):
    return sum(sum(filter(None, r)) for r in b)


def p1():
    games = deepcopy(boards)
    for n in numbers:
        for b in games:
            if mark(b, n) and win(b):
                return n * score(b)


def p2():
    last_winning_move, last_score = 0, 0
    for b in deepcopy(boards):
        for move, n in enumerate(numbers):
            if mark(b, n) and win(b):
                break
        if move > last_winning_move:
            last_winning_move, last_score = move, n * score(b)
    return last_score


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)
