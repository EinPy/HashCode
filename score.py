from dataparser import *
from collections import *

# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer
def score(inp, out):
    ns = parse(inp)
    itr = (line for line in out.split('\n'))
    D = ni(itr)
    assert 1 <= D <= ns.T2 + ns.T3 + ns.T4
    used = set()
    SC = 0
    for _ in range(D):
        L, *pz = nl(itr)
        assert 2 <= L <= 4
        assert L == len(pz)
        ingrSet = set()
        for p in pz:
            assert p not in used
            used.add(p)
            assert 0 <= p < ns.M
            for ing in  ns.pizzas[p]['ing']:
                ingrSet.add(ing)
        SC += len(ingrSet)**2

    return SC


