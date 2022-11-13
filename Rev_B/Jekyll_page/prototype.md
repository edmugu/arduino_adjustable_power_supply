---
layout: default
title: Prototype
nav_order: 3
parent: Rev B0
---
## Bread board prototypes. 
I started doing sanity checks on my breadboard before designing the PCB. Moreover, even though I could not run them at high power [as shown below]. It revealed some of the design issues I should have caught in the simulation phase.  
![Burned BreadBoard](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Jekyll_page/snips/breadboard.PNG "Very Hot Transistor")



## Issue Solved #1: TI's voltage regulator below 1.2V requires a minimum current 

When I breadboarded this with an adjustable linear regulator that can only push current, the output never went below 1.2 V. The reason is that when the Vref_ext is held above 1.2 V, the Reg will start to "shut down" and leave the output pin floating. So the output will be the same as Vref_ext since there is no current across R_bot and R_top. To overcome this, one needs a minimum current at Vout to drop 1.2V across R_top. 



Also, since the voltage will be either controlled by external resistors OR the external voltage reference. The regulator will have to switch between these two modes of operation. If the desired voltage is above 2.4 V, the external resistors will control the regulator, and it will behave like a normal regulator. However, if the desired voltage is below 2.4V, it will slowly turn on Vref_ext, keeping R_top and R_bot the same. This will force the main regulator to shutdown.  

![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/TI_below_1V2.PNG)
