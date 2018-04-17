import os, sys
import secrets, random
import string
from itertools import groupby
from operator import itemgetter

if not os.path.isfile('nouns.txt') or not os.path.isfile('adjectives.txt'):
    sys.exit(1)

length_min = 8
length_max = 0
total = 5
rand_ord = False
rand_sym = False

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
        elif sys.argv[i] == '-r':
            rand_ord = True
        elif sys.argv[i] == '-R':
            rand_sym = True
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
    rn = secrets.randbelow(len(nouns))
    n = nouns[rn]

    ra = secrets.randbelow(len(adjct))
    a1 = adjct[list(adjct.keys())[ra]]
    a1 = a1[secrets.randbelow(len(a1))]

    if not rand_ord:
        a2 = adjct[list(adjct.keys())[ra]]
        a2 = a2[secrets.randbelow(len(a2))]
    else:
        ra = secrets.randbelow(len(adjct))
        a2 = adjct[list(adjct.keys())[ra]]
        a2 = a2[secrets.randbelow(len(a2))]

    if a1 < a2:
        pwd = f'{a1} {a2} {n}'.title()
    else:
        pwd = f'{a2} {a1} {n}'.title()

    if pwd not in pwds:
        if len(pwd.replace(' ', '')) >= length_min:
            if length_max and len(pwd.replace(' ', '')) <= length_max:
                pwds.append(pwd)
            elif not length_max:
                pwds.append(pwd)
    i += 1

pwds.sort()

if rand_sym:
    symbols = list(string.digits + string.punctuation)
    random.shuffle(symbols)

    for i in range(0, len(pwds)):
        pwd = list(pwds[i].replace(' ', '').lower())
        for j in range(0, secrets.randbelow(len(pwd))+1):
            while True:
                x = secrets.choice(range(0, len(pwd)))
                if random.random() >= 0.5: break
            pwd[j] = secrets.choice(symbols)
        for j in range(0, secrets.randbelow(len(pwd))+1):
            while True:
                x = secrets.choice(range(0, len(pwd)))
                if random.random() >= 0.5: break
            pwd[j] = pwd[j].upper()
        pwds[i] = ''.join(pwd)

print('\n'.join(pwds))
