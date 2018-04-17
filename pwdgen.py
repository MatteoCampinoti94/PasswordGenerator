import os, sys
import random
from itertools import groupby
from operator import itemgetter

with open("nouns.txt", "r") as f:
	nouns = f.readlines()
	nouns = [n.lower().strip() for n in nouns if len(n.strip())]
	nouns.sort()


with open("adjectives.txt", "r") as f:
	adjct = f.readlines()
	adjct = [a.lower().strip() for a in adjct if len(a.strip())]
	adjct.sort()
	adjct = {k: list(v) for k,v in groupby(adjct, itemgetter(0))}

pwds = []
while len(pwds) < 5:
    r = random.randint(0, len(nouns)-1)
    n = nouns[r]

    r = random.randint(0, len(adjct)-1)
    a = list(adjct.keys())[r]

    r1 = random.randint(0, len(adjct[a])-1)
    while True:
        r2 = random.randint(0, len(adjct[a])-1)
        if r2 != r1: break

    if r1 < r2:
        pwd = f'{adjct[a][r1]} {adjct[a][r2]} {n}'.title()
    else:
        pwd = f'{adjct[a][r2]} {adjct[a][r1]} {n}'.title()

    if pwd not in pwds:
        pwds.append(pwd)

pwds.sort()
print('\n'.join(pwds))
