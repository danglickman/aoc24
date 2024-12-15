import re
import numpy as np
import scipy as sp

with open('input') as f:
    input = f.read().strip()

ar = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
br = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
pr = re.compile(r"Prize: X=(\d+), Y=(\d+)")

p1 = 0
p2 = 0
entries = input.split('\n\n')
for entry in entries:
    m = ar.search(entry)
    As = [int(i) for i in m.groups()]
    m = br.search(entry)
    Bs = [int(i) for i in m.groups()]
    m = pr.search(entry)
    P = [int(i) for i in m.groups()]
    buttons = np.array([As, Bs]).T
    P = np.array(P)

    # it's probably not necessary to us sp.optimize but want to try it
    # indeed, easy to compute solution and check integrality or if singular reduce to button A and do the same
    solve = sp.optimize.linprog(np.array([3, 1]), A_eq = buttons, b_eq = P, integrality=np.ones(2))
    if solve.success:
        p1 += solve.fun

    P += np.array([10000000000000, 10000000000000])
    # only correct with presolve disabled
    solve = sp.optimize.linprog(np.array([3, 1]), A_eq = buttons, b_eq = P, integrality=np.ones(2), options= {"presolve":False})
    if solve.success:
        p2 += solve.fun

print(np.rint(p1))
print(p2)