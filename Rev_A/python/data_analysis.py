# -*- coding: utf-8 -*-
"""
Created on Sun May 18 2021

Simple data analysis script



@author: Eduardo Munoz
@email: edmugu@protonmail.com
"""
import matplotlib.pyplot as plt
import pandas as pd
import os

dir1 = "../measurements/"


for filename in os.listdir(dir1):
    if filename.endswith(".csv"):
        file = dir1 + filename
        df = pd.read_csv(file)
        
        fig, ax1 = plt.subplots()
        color = 'tab:blue'
        x = list(df["Iout_meas [A]"])
        y = list(df["Iin_meas [A]"])
        plt.plot(x, y, color=color)
        plt.suptitle(file)
        plt.title("Iin and Vout vs Iout")
        plt.xlabel("Iout [Amps]")
        plt.ylabel("Iin [Amps]", color=color)
        plt.axhline(y=1.0, color="black")
        
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        
        y = list(df["Vout_meas [V]"])
        x = list(df["Iout_meas [A]"])
        
        color = 'tab:red'
        plt.plot(x, y, color=color)
        plt.ylabel("Vout [Volts]", color=color)
        
        
        plt.savefig(file + ".png")