import os, sys
import secrets
from itertools import groupby
from operator import itemgetter

if not os.path.isfile('nouns.txt') or not os.path.isfile('adjectives.txt'):
    sys.exit(1)

length_min = 8
length_max = 0
total = 5

if len(sys.argv) > 1:
    i = 0
    while i < len(sys.argv):
        if sys.argv[i] == '-l' and i < len(sys.argv)-1:
            try:
                length_min = int(sys.argv[i+1])
            except:
                length_min = 8
            i += 1
        elif sys.argv[i] == '-t' and i < len(sys.argv)-1:
            try:
                total = int(sys.argv[i+1])
            except:
                total = 5
            i += 1
        elif sys.argv[i] == '-L' and i < len(sys.argv)-1:
            try:
                length_max = int(sys.argv[i+1])
            except:
                length_max = 0
            i += 1
        elif sys.argv[i] == '-ll' and i < len(sys.argv)-1:
            try:
                length_min = int(sys.argv[i+1])
                length_max = int(sys.argv[i+1])
            except:
                length_min = 8
                length_max = 0
            i += 1
        i += 1

if (length_max != 0 and length_max < length_min) or length_min < 0:
    sys.exit(2)

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
i = 0
while len(pwds) < total and i < 100000:
    r = secrets.randbelow(len(nouns))
    n = nouns[r]

    r = secrets.randbelow(len(adjct))
    a = list(adjct.keys())[r]

    r1 = secrets.randbelow(len(adjct[a]))
    while True:
        r2 = secrets.randbelow(len(adjct[a]))
        if r2 != r1: break

    if r1 < r2:
        pwd = f'{adjct[a][r1]} {adjct[a][r2]} {n}'.title()
    else:
        pwd = f'{adjct[a][r2]} {adjct[a][r1]} {n}'.title()

    if pwd not in pwds:
        if len(pwd.replace(' ', '')) >= length_min:
            if length_max and len(pwd.replace(' ', '')) <= length_max:
                pwds.append(pwd)
            elif not length_max:
                pwds.append(pwd)
    i += 1

pwds.sort()
print('\n'.join(pwds))
