---
title: Debugging
has_children: no
nav_order: 2
parent: Rev A0
---



# Debugging Process
## Bug 1: The voltage of the first stage does not go above Vin
After checking that the enable pin was high and that the switching output was doing what it was supposed to be doing, I decided to replace the IC. However, it still showed the same behavior. First, Vout would reach >30 Volts; then it would drop to Vin. Then I checked my IC units on an eval board, and they work. At that moment, I started to investigate the second most complicated unit on the first stage, the diode. Then it was clear that the issue was that I installed the diode backward. However, the silkscreen and schematics had the diode in the right orientation. So that meant the footprint pads of the diode were swapped.

![board bring up](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/picture%20of%20bringup.PNG  "board bring up")

![diode zoomed](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/diode_zoomed.PNG  "diode zoomed")



## Bug 2: The output of the final stage was stuck at 1.8 Volts
Note that the feedback to the last two stages can be selected between a "fixed" voltage divided that would allow the output to go all the way to 27 volts. Or it can be selected to be the dynamic feedback circuit that would keep the voltage of the last two stages close to each other. The circuit worked fine when a fixed voltage divider was used; however, it got stuck at 1.8 volts when it was switch to the dynamic feedback. At that moment, the feedback circuit was set to have a 0.8 Volts difference between the two stages. And indeed, there was a 0.8-volt difference between the stages. So I thought that maybe if I raised the difference to 5 volts, it would work. Luckily, it did, and after looking for an explanation, I noted that the linear regulator needed at least a 3 volts difference between its output and its input. 
	
## Bug 3: The output can only drive <1 mA before it starts to struggle. 
I believed this is due to the SMD capacitors. However, I noted that this issue went away if I lowered the voltage to the minimum voltage of 1.2V and then raised it to the wanted voltage. So it seems that the step-down switch and regulator had issues if the initial load was too much. So I decided to make a prototype out of evaluation boards to check this behavior because my board already had a compromising rework on the Schottky diodes. When I characterized the prototype, it was only able to output 5 Watts when the design should have had been able to handle >10 Watts. 

A few notes on the prototype: 
	(1) the evaluation board of the step-down circuit is for the LMR14006 component, but it has the same pinout as the AOZ1282. So the unit was swapped.
	(2) the wires used are size AWG 20, and they can handle 1.5 amps; this should not be a limiting factor yet.
	
![prototype out of eval boards](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/debugging.PNG  "prototype out of eval boards")

