---
layout: default
title: Simulation
nav_order: 3
parent: Rev. B
---

# Intro to Simulation study 

In short, I have learned that to design a power circuit right you have to use the SPICE tools of the PROs [i.e. Texas Instruments and Analog Devices]. Their tools will have the proper model for the components they sell and the supporting components they used to test their devices. So their SPICE simulations will be far better than the ones and average engineer can do by importing models or making pseudo models of the components they plan to use. With that out the way, the following are the simulations "learning nuggets" I have come acrossed. 

## Issue avoided #1: External Reference too noisy

At the beginning, it seemed that hooking Vref_ext as a voltage divider and voltage buffer would be a good idea. Well, it turns out that the noise of Vin and voltage buffer "noise" is able to getting in Vout. So buffer would not be a good idea. 

![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/TI_below_1V2.PNG)



## Issue avoided #2: LT1575 with "virtual ground"

During simulation it was found that the gate driver is not directly connected to ground and therefore, the gate will always be held above ~2.0 Volts. Which means it will not allow you to output a voltage below 1.2V even if you use the "TI's external voltage reference" modification.

![LT1575 virtual ground](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/LT1575_issue.PNG)

So I will have to use a part not from analog devices. The MIC5156 does have a gate driver capable of going to 0 zero volts. 

![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/MIC5156_fix.PNG)



