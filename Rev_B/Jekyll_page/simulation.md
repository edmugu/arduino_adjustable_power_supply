# Intro to the Simulation study 

In short, I have learned that to design a power circuit right; you have to use the SPICE tools of the PROs [i.e., Texas Instruments and Analog Devices]. Their tools will have the proper model for the components they sell and the supporting components they used to test their devices. So their SPICE simulations will be far better than the ones, and average engineers can do by importing models or making pseudo models of the components they plan to use. The following are the simulations "learning nuggets" I have come across with that out the way. 

## Issue Solved #1: External Reference too noisy

In the beginning, it seemed that hooking Vref_ext as a voltage divider and voltage buffer would be a good idea. However, it turns out that the noise of Vin and voltage buffer "noise" can get in Vout. So buffer would not be a good idea. 

![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/TI_below_1V2.PNG)



## Issue Solved #2: LT1575 with "virtual ground"

During simulation, it was found that the gate driver is not directly connected to the ground, and therefore, the gate will always be held above ~2.0 Volts. Unfortunately, this means it will not allow you to output a voltage below 1.2V even if you use the "TI's external voltage reference" modification.

![LT1575 virtual ground](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/LT1575_issue.PNG)

So I will have to use a part, not from analog devices. However, the MIC5156 does have a gate driver capable of going down to 1 volt at the gate voltage. Now, there are plenty of MOSFETs with a gate threshold above 1 volt. 

![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/MIC5156_fix.PNG)



## Issue Solved #3: Proper Capacitor 

During simulation, I discovered why the Tantalum capacitor is bad for power supplies. The reason is that these capacitors have an "equivalent series resistance" around a few ohms. So one can't draw a few amps without having a significant voltage drop. That is why you should use Aluminum Electrolytic Capacitors since their ESR is in the milliohm range. 
