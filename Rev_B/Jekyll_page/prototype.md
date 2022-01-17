---
layout: default
title: Prototype
nav_order: 4
parent: Rev. B
---
## Bread board prototypes. 
After doing some sanity test on the new modules on a bread board, I wanted to do some stress testing. However, the plastic on the bread board can't handle over a watt of heat a transistor can generate while I tested the 10+ watt output I wanted.
![Burned BreadBoard](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Jekyll_page/snips/breadboard.PNG "Very Hot Transistor")


## Perfboard prototypes. 
So I decided to do a success full stress test before I design the PCB for this project. So I moved to the perfboards that can take much more heat. 

![Prototype boads](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Jekyll_page/snips/prototype_board.PNG "Pretty prototype Boards")



## Issue Solved #1: TI's voltage regulator below 1.2V requires a minimum current 

When I breadboarded this, with a adjustable linear regulator that can only push current, the output never when below 1.2V . The reason is that when the Vref_ext was held above 1.2V the Reg will start to "shutdown" and leave the output pin floating. So if is left floating the voltage on the output will be the same as Vref_ext, since there is no current across Rbot and Rtop. To overcome this, you need a minimum current at Vout to drop 1.2V across Rtop. 

Now the operation of this regulator is to behave normally for voltages above 2.4Volts. Once the regulator wants to go below 2.4V, it will slowly turn on Vref_ext keeping Rtop and Rbot the same. That way the average of Vout and Vref_ext will be the 1.2Volts. 

![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/TI_below_1V2.PNG)
