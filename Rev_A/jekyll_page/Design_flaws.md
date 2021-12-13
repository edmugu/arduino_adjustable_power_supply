---
title: Design Flaws
has_children: no
nav_order: 7
parent: Rev. A
---



# Design Flaws

## How much current can be drawn in and drawn out

The main mistake I made was on the step-up stage. I expected this stage to be able to handle 1 amp current since the datasheet of the step-up regulator mention that this was a **"40Vout, 1A Step-Up voltage regulator."\** However, current can only be achieved when the output voltage is close to the input voltage, as shown in the figures below. Now in figure 10, one can see that when the input voltage is 3.3Volts, and the output voltage is 15Volts, the output current will be less than 200 mA. The reason is that the regulator can only handle 1 Amp. So it can only output the 3.3 Watts it gets in [ = 3.3 Volts * 1 amp]. This means it can only deliver a maximum of 0.22 Amps [= 3.3 watts / 15 volts ]. And in top of that the regultor is >60% efficent at that point so one would only get  0.132 Amps [= 0.22 Amps * 0.60].

![LMR64010 current chart](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/lmr64010_current_chart.PNG)

So if I wanted a regulator that could deliver 1 amp at 36 Volts, I would have needed a regulator that could handle >36 Watts at its lowest voltage of 2.7 Volts, which means that the regulator needed to handle at least 13.333 Amps. Unfortunately, the power banks I have seen can only handle a max of 2.1 - 3 Amps so I going to limit the current to that. 







