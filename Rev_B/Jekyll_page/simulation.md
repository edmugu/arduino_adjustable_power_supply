---
layout: default
title: Simulation
nav_order: 3
parent: Rev. B
---

# Intro to Simulation study 

I have learned that to do this right you have to use the SPICE tools of the pros [i.e. Texas Instruments and Analog Devices]. Their tools will have the proper model for the components they sell and the supporting components they used. So their SPICE simulations will be far better than the one I can do by importing models or making models of the components I plan to use. With that out the way, the following are the simulations I have done and the "learning nuggets" I have come across. 



# Stage 3: Linear Regulator Controller

For the LT1575 one can see two major issues (1) Vout <= Vin - Vth, where Vth is the threshold voltage of the power MOSFET and (2) Vin <= 22 Volts. So If I want to the power supply to at least output 22 Volts I need a MOSFET with low Vth. 

![LT1575 snip from datasheet](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/LT1575.PNG "LT1575 snip")



## "Heat" measurements

During simulation, it was found that the LT1575 will burn off up to 4 watts on the steady state. 

