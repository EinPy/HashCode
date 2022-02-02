import argparse
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
    out = []
    for i in range(ns.T4):
        if len(left) < 4: break
        msg = ['4']
        for _ in range(4):
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
