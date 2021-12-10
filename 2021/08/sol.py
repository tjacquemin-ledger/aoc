input = open('input', 'r').read().strip()
input = [[list(map(frozenset, x.split())) for x in r.split('|')] for r in input.splitlines()]


# Preparing smart key table based on fixed digits
segments = list(map(frozenset, 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'.split()))

count = {}
for n, seg in enumerate(segments): count.setdefault(len(seg), []).append(seg)
fixed = {lgt: count[lgt][0] for lgt in sorted(count) if len(count[lgt]) == 1}

key = lambda s, f: tuple(len(x & s) for x in f)
table = {key(seg, fixed.values()): str(n) for n, seg in enumerate(segments)}
assert len(table) == 10


def p1():
    return sum(len(x) in fixed for _, o in input for x in o)


def p2():
    def decode(i, o):
        f = sorted((s for s in i if len(s) in fixed), key=len)
        t = {s: key(s, f) for s in i}
        return int(''.join(table[t[s]] for s in o))
    return sum(decode(i, o) for i, o in input)


if (r1 := p1()) is not None: print(r1)
if (r2 := p2()) is not None: print(r2)


# def p2():
#     # From observation
#     def decode(i, o):
#         fixed = {}
#         for d in i:
#             if len(d) == 2: fixed[1] = set(d)
#             if len(d) == 3: fixed[7] = set(d)
#             if len(d) == 4: fixed[4] = set(d)
#             if len(d) == 7: fixed[8] = set(d)
#
#         mapping = {}
#         for d in i:
#             if len(d) == 2: mapping[d] = '1'
#             if len(d) == 3: mapping[d] = '7'
#             if len(d) == 4: mapping[d] = '4'
#             if len(d) == 7: mapping[d] = '8'
#             if len(d) == 5:
#                 if len(fixed[4].intersection(d)) == 2: mapping[d] = '2'
#                 elif len(fixed[1].intersection(d)) == 2: mapping[d] = '3'
#                 else: mapping[d] = '5'
#             if len(d) == 6:
#                 if fixed[4].issubset(d): mapping[d] = '9'
#                 elif fixed[1].issubset(d): mapping[d] = '0'
#                 else: mapping[d] = '6'
#         return int(''.join(map(mapping.get, o)))
#
#     return sum(decode(i, o) for i, o in input)


# Search without smart key through successive pruning
#
# from collections import defaultdict
# from typing import List
#
#
#
# def count_simple_outputs(patterns: List[List[str]]) -> int:
#     return sum(1 for p in patterns for x in p[1] if len(x) in {2, 3, 4, 7})
#
#
# def translate_outputs(patterns: List[List[str]]) -> List[int]:
#     # which segments are active for each digit
#     wire_map = {
#         0: {0, 1, 2, 4, 5, 6},
#         1: {2, 5},
#         2: {0, 2, 3, 4, 6},
#         3: {0, 2, 3, 5, 6},
#         4: {1, 2, 3, 5},
#         5: {0, 1, 3, 5, 6},
#         6: {0, 1, 3, 4, 5, 6},
#         7: {0, 2, 5},
#         8: {0, 1, 2, 3, 4, 5, 6},
#         9: {0, 1, 2, 3, 5, 6}
#     }
#
#     # group digits by the number of segments lit in each digit
#     wire_len_map = defaultdict(set)
#     for k, v in wire_map.items():
#         wire_len_map[len(v)].add(k)
#
#     outputs = []
#     for [tests, digits] in patterns:
#
#         # for our initial candidate, every segment could be lit
#         # by every possible signal
#         wire = [{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'} for _ in range(7)]
#         wires = [wire]
#
#         for test in tests:
#             new_wires = []
#
#             candidates = wire_len_map[len(test)]
#
#             for n in candidates:
#                 for wire in wires:
#                     new_wire = [wire[i] & set(test) if i in wire_map[n] else wire[i] for i in range(7)]
#
#                     # run over each segment and make sure that any segment with
#                     # only 1 remaining candidate is not part of any other segment
#                     for i in range(7):
#                         if len(new_wire[i]) == 1:
#                             new_wire = [new_wire[x] - set(new_wire[i]) if i != x else new_wire[x] for x in
#                                         range(7)]
#
#                     # the wire is only valid if each segment still has at least 1
#                     # candidate signal
#                     if all([len(x) > 0 for x in new_wire]):
#                         new_wires.append(new_wire)
#
#             wires = new_wires
#
#         wire_remap = {list(wires[0][n])[0]: n for n in range(7)}
#
#         output = 0
#         for digit in digits:
#             segments = {wire_remap[x] for x in digit}
#             for n in wire_map:
#                 if wire_map[n] == segments:
#                     output = output * 10 + n
#                     break
#
#         outputs.append(output)
#
#     return outputs
#
#
# def run() -> None:
#     patterns = []
#     for line in open('input').readlines():
#         tests, digits = (x.split() for x in line.strip().split(" | "))
#         patterns.append([sorted(tests, key=lambda x: len(x)), digits])
#
#     print(f'Simple output count: {count_simple_outputs(patterns)}')
#
#     outputs = translate_outputs(patterns)
#     print(f"Output sum: {sum(outputs)}\nOutputs:\n{outputs})")
#
#
# if __name__ == '__main__':
#     run()
