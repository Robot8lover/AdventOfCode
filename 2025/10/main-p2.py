import sys; sys.dont_write_bytecode = True; from utils import *
from scipy import optimize
from scipy.optimize import milp
import numpy as np
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
        target_voltages = [int(v) for v in groups[2].split(",")]
        num_voltages = len(target_voltages)
        wiring = [[int(c) for c in v[1:-1].split(",")] for v in groups[1].split()]
        wiring_vecs = []
        for t in wiring:
            vec = [0] * num_voltages
            for v in t:
                vec[v] = 1
            wiring_vecs.append(vec)

        epsilon = 1e-9
        lower = np.array(target_voltages) - epsilon
        upper = np.array(target_voltages) + epsilon

        function_coefficients = np.ones(len(wiring_vecs))
        wiring_vecs_array = np.array(wiring_vecs).transpose()
        bounds = optimize.Bounds(0, int(sum(target_voltages)))
        integrality = np.full_like(function_coefficients, True)
        constraints = optimize.LinearConstraint(A=wiring_vecs_array, lb=lower, ub=upper)

        result = milp(c=function_coefficients, constraints=constraints, integrality=integrality, bounds=bounds)
        if result.status:
            print(result)

        total += int(round(result.fun))

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