# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:02:19 2021

It simulates the output of the linear regulator output.

@author: Eduardo Munoz
@email: edmugu@protonmail.com
"""
import time
import pandas as pd
import matplotlib.pyplot as plt

Rtaps = 8
Vrefext = 3.3

tlist = list(range(0, Rtaps + 1))
vlist = list(map(lambda x: Vrefext * x / Rtaps, range(1, Rtaps + 1)))

def voutadj(t, v, vint=1.2):
    ratio = t/Rtaps
    ans = vint * (1 + ratio) - (ratio * v)
    return ans

def vout(t, vint=1.2):
    ratio = t/Rtaps
    ans = vint * (1 + ratio)
    return ans

for v in vlist:
    vdata = [("tap", "voutadj", "vout")]
    for t in tlist:
        vdata.append((t, voutadj(t, v), vout(t)))
    df = pd.DataFrame(vdata)

    print("\nfor v = %3.5f \n" % v)
    print(df)




