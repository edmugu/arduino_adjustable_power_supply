---
layout: default
title: Prototype
nav_order: 3
parent: Rev. B
---
## Bread board prototypes. 
I started to do some sanity checks on my bread board before I designed the PCB. And even thought I could not run them at high power [as shown below]. It did revealed some of the issues on the design I did not catched on the simulation phase. 
![Burned BreadBoard](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Jekyll_page/snips/breadboard.PNG "Very Hot Transistor")



## Issue Solved #1: TI's voltage regulator below 1.2V requires a minimum current 

When I breadboarded this, with a adjustable linear regulator that can only push current, the output never when below 1.2V . The reason is that when the Vref_ext was held above 1.2V the Reg will start to "shutdown" and leave the output pin floating. So if is left floating the voltage on the output will be the same as Vref_ext, since there is no current across Rbot and Rtop. To overcome this, you need a minimum current at Vout to drop 1.2V across Rtop. 

Now the operation of this regulator is to behave normally for voltages above 2.4Volts. Once the regulator wants to go below 2.4V, it will slowly turn on Vref_ext keeping Rtop and Rbot the same. That way the average of Vout and Vref_ext will be the 1.2Volts. 

![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/TI_below_1V2.PNG)
