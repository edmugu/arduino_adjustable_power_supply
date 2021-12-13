# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:02:19 2021

It simulates the output of the linear regulator output.

@author: Eduardo Munoz
@email: edmugu@protonmail.com
"""
import pandas as pd
import matplotlib.pyplot as plt

Ra = 0
Rb = 10000

rlist = list(map(lambda x: Rb * x/10.0, range(0, 10)))

def vout(r, Ra=Ra, Rb=Rb, Vref = 1.25, Iadj=50e-6):
    R2 = r
    R1 = Ra + Rb - r
    #R1 = Ra
    
    ans = Vref * (1 + (R2/R1)) + Iadj * R2
    return ans


vo = []

for r in rlist: 
    vo.append(vout(r))
    

plt.plot(rlist, vo)
