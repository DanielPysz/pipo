#!/usr/bin/env python3

import sys

# ATOM   3781  CA  ALA B 446      23.368 -12.536  -7.742  1.00  0.00           C

i_model = 0
i_atom = 0
plik = None
for line in open(sys.argv[1]):
    if line.startswith("MODEL"): 
        i_model+=1
        if plik: plik.close()
        plik = open(f"{i_model}.xyz", "w")
        i_atom = 0
    if not line.startswith("ATOM "): continue
    if not line[13:15] == "CA": continue
    x = float(line[30:38].strip())
    y = float(line[38:46].strip())
    z = float(line[46:54].strip())
    print(i_atom, x,y,z,file=plik)
    i_atom += 1
        
plik.close()