---
layout: default
title: PCB
nav_order: 4
parent: Rev. B
---

# PCB

Before I pick any case I wanted to "modularize" each of the stages to have an idea of how much space I needed. Also, to get better temperature readings of the MOSFET it seems that having two MOSFETS in "parallel" would distribute the heat propagated. And a thermal resistor could be placed in between, with some thermal paste, that way the temperature readings would be more accurate. 



At the moment, it seems that 2 inches x 2 inches will be good enough per stage [not counting heat sink area]. So I will probably need a case 10 inches x 4 inches. 



## Thermal sensors



![n-mos](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/n-mos.PNG)

In addition to having a single thermistor circuit, there will be another pair of resistors as reference. That way a differential pair can be made and the measurements will be more accurate. 



## Test points

I have been wanting to add proper "high speed" test points that are 50 ohms, so I could hook a high-end scope to the various stages of the design. Since connecting the 50-ohm probe to the voltage rails would overwhelm the controllers/regulators, I used a π-matching circuit. The image below shows such a circuit below. Note that even R48 is not really needed, I left it for "good luck/practice." 



![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/matching_pi_circuit.PNG)



## Encoders instead of Potentiometers

I have been also wanting to add encoders since they have an unlimited turn count. One for voltage and one for current limit. 

![](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/schematics_encoder.PNG)





## Final PDF

https://github.com/edmugu/arduino_adjustable_power_supply/blob/master/Rev_B/Jekyll_page/PCB.pdf

<object data="https://github.com/edmugu/arduino_adjustable_power_supply/blob/master/Rev_B/Jekyll_page/PCB.pdf" width="1000" height="1000" type='application/pdf'></object>
