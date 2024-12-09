import sys; sys.dont_write_bytecode = True; from utils import *
"""
To do: ensure Code Runner works, have preloaded the day and input in Chrome,
saved input into the folder, have utils on the side, collapse regions

Strings, lists, dicts:
lmap, ints, positive_ints, floats, positive_floats, words, keyvalues

Algorithms:
bisect, binary_search, hamming_distance, edit_distance

Data structures:
Linked, UnionFind
use deque for queue: q[0], q.append and q.popleft

List/Vector operations:
GRID_DELTA, OCT_DELTA
lget, lset, fst, snd
padd, pneg, psub, pmul, pdot, pdist1, pdist2sq, pdist2

Matrices:
matmat, matvec, matexp

Previous problems:
knot

Dict things:
dict.keys()
dict.values()
dict.items()
"""

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    result = 0
    for line in lines:
        disk = []
        empty = []
        files = {}
        file_count = 0
        ind = 0
        for i, c in enumerate(line):
            n = int(c)
            if i & 1:
                # empty
                empty.append([ind, n])
                disk.extend([None] * n)
                ind += n
            else:
                # file
                files[i // 2] = [ind, n]
                disk.extend([i // 2] * n)
                file_count += n
                ind += n

        empty.reverse() # perhaps more efficient pop?

        sprint(empty)
        sprint(files)

        files_to_go = list(reversed(range(len(files))))
        while files_to_go and empty:
            sprint(files_to_go)
            sprint(empty)
            used = False
            for id_num in files_to_go:
                file_ind, size = files[id_num]
                empty_ind, empty_size = empty[-1]
                if file_ind < empty_ind:
                    break
                fix_empty = False
                if empty_size == size:
                    files[id_num][0] = empty_ind
                    empty.pop()
                    used = True
                    fix_empty = True
                elif empty_size > size:
                    empty[-1][0] += size
                    empty[-1][1] -= size
                    files[id_num][0] = empty_ind
                    used = True
                    fix_empty = True

                if fix_empty:
                    files_to_go.pop(files_to_go.index(id_num))
                    after = file_ind + size
                    tar = -1
                    for i in range(len(empty)):
                        if empty[i][0] == after:
                            tar = i
                            break
                    if tar > 0:
                        rem_ind, rem_size = empty[tar - 1]
                        if rem_ind + rem_size == file_ind:
                            empty.pop(tar - 1)
                        else:
                            rem_ind, rem_size = (0, 0)
                    else:
                        rem_ind, rem_size = (0, 0)

                    if tar > -1:
                        empty[tar][1] += rem_size + size
                    else:
                        for i, (bef_ind, bef_size) in enumerate(empty):
                            if bef_ind + bef_size == file_ind:
                                empty[i][1] += size
                                break

                    break
            if not used:
                empty.pop()

        sprint(disk)
        disk = [None] * len(disk)
        for id_num, (index, size) in files.items():
            for i in range(size):
                disk[i + index] = id_num
        sprint(disk)

        for id_num, (index, size) in files.items():
            for i in range(size):
                result += id_num * (i + index)


    print(result)


    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
2333133121414131402
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