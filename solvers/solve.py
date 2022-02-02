import argparse
import curses
import random
import sys
sys.path.extend(['..', '.'])
from collections import *
from dataparser import parse
from util import get_in_file_content

# inp is an input file as a single string
# return your output as a string

def solve(inp, args):
    # TODO: Solve the problem
    random.seed(args['seed'])
    ns = parse(inp)
    left = list(range(ns.M))
    left.sort(key=lambda i: len(ns.pizzas[i]['ing']))
    out = []
    for i in range(ns.T4):
        if len(left) < 4: break
        msg = ['4']
        best = 0
        inds = [0,0]
        interval = 10
        if len(left) > interval+5:
            for a in range(len(left)-1, len(left)-interval,-1):
                for j in range(a, len(left)-interval,-1):
                    curSet = set()
                    for el in ns.pizzas[a]['ing']:
                        curSet.add(el)
                    for el in ns.pizzas[j]['ing']:
                        curSet.add(el)
                    best = max(best, len(curSet))
                    if best == len(curSet):
                        inds[0],inds[0] = a, j
            msg.append(str(left.pop(inds[0])))
            msg.append(str(left.pop(inds[1])))
            for _ in range(2):
                msg.append(str(left.pop()))
        else:
            for _ in range(4):
                msg.append(str(left.pop()))
            out.append(' '.join(msg))
    if len(left) == 3:
        msg = ['3']
        for _ in range(3):
            msg.append(str(left.pop()))
        out.append(' '.join(msg))
    if len(left) == 2:
        msg = ['2']
        for _ in range(2):
            msg.append(str(left.pop()))
        out.append(' '.join(msg))
    
    out = [str(len(out))] + out

    return '\n'.join(out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('in_file')
    args = parser.parse_args()
    inp = get_in_file_content(args.in_file)
    out = solve(inp, {'seed': 0})
    print('\n'.join(['OUT:', '=========', out]))
