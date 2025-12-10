import sys; sys.dont_write_bytecode = True; from utils import *
from scipy.optimize import milp
"""
To do: ensure Code Runner works, have preloaded the day and input in Chrome,
saved input into the folder, have utils on the side, collapse regions

Strings, lists, dicts:
lmap, min_max, max_minus_min

Algorithms:
bisect, binary_search, hamming_distance, edit_distance

Data structures:

List/Vector operations:

Matrices:

Previous problems:

Dict things:
dict.keys()
dict.values()
dict.items()
"""

def xor_vecs(u, v):
    result = []   # left aligned
    if len(u) > len(v):
        result = u[:]
        for i, n in enumerate(v):
            result[i] ^= n
    else:
        result = v[:]
        for i, n in enumerate(u):
            result[i] ^= n
    return tuple(result)

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    total = 0
    for line in lines:
        pattern = r"\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}"
        groups = re.match(pattern, line).groups()
        target_lights = tuple(1 if c == "#" else 0 for c in groups[0])
        num_lights = len(target_lights)
        wiring = [tuple(int(c) for c in v[1:-1].split(",")) for v in groups[1].split()]
        wiring_vecs = []
        for t in wiring:
            vec = [0] * num_lights
            for v in t:
                vec[v] = 1
            wiring_vecs.append(vec)
        target_voltages = tuple(int(v) for v in groups[2][-1:1].split(","))

        # if light is on, negative voltage must be less than or equal to negative of target voltage
        # if light is off, voltage must be strictly less than target voltage,
        # so less than or equal to target voltage - 1
        for i, tl in enumerate(target_lights):
            if tl:
                wiring_vecs[i] = -wiring_vecs[i]
                target_voltages[i] = -target_voltages[i]
            else:
                target_voltages[i] = target_voltages[i] - 1


        """
        Integer Linear Programming
        x in Z^n
        maximize [-1 -1 -1 -1 ...]^T * x (or minimize x)
        subject to wiring_vecs*x + s = target_voltages (alternatively wiring_vecs*x <= target_voltages)
        s >= 0
        x >= 0
        """

        def check(voltages):
            for i in range(len(target_voltages)):
                if voltages[i] != target_voltages[i]:
                    return False
                return True

        done = False
        for r in range(1, len(wiring_vecs)):
            for perm in itertools.permutations(wiring_vecs, r):
                voltages = [0] * len(target_lights)
                for button_vec in perm:
                    lights = xor_vecs(lights, button_vec)
                if check(voltages)
                    done = True
            if done:
                total += r
                break
    print(total)



    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""],[
# Part 2
r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case) # day and year can be added as arguments if not doing today