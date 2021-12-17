---
layout: default
title: Simulation
nav_order: 3
parent: Rev. B
---

# Intro to Simulation study 

In short, I have learned that to design a power circuit right you have to use the SPICE tools of the PROs [i.e. Texas Instruments and Analog Devices]. Their tools will have the proper model for the components they sell and the supporting components they used to test their devices. So their SPICE simulations will be far better than the ones and average engineer can do by importing models or making pseudo models of the components they plan to use. With that out the way, the following are the simulations I have done and the "learning nuggets" I have come across. Also while simulating this, it appear that the output requirements seem to be driving this most of the time, so I will start with the output stage and go backwards through the design. 



# Stage 3: Linear Regulator Controller

This is the last stage [besides the reverse current protection] and it is probably the most complicated part of the design. But the bottom line is that this stage will burn off some of buck converter output and will leave a clean output on Vout. But to achieve that, the controller, ideally, will require two Voltage inputs. Vboost will drive the controller logic and has to be at least 2 Volts above Vout so it can drive the MOSFET properly. However, Vbuck will deliver all the power going to Vout and has to be close to Vout so that the MOSFET does not have to work as hard, burning off the unwanted voltage. This is shown on the image below. 

![Stage3](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/stage3a.PNG )

The hard part of the design is the complex feedback circuit. This circuit comes from a ["Texas instruments" article]("https://github.com/edmugu/arduino_adjustable_power_supply/blob/master/documentation/TI_Below_1V2.pdf") that does a good job explaining it. However, this circuit was made to work on two states: (state 1) Vref_buf is 0V, and this circuit works as normal, and (state 2) Vref_buf is not 0V BUT R10 and R11 are equal, so the average between Vout and Vref_buf has to be 1.2 Volts.  

When the device is on state 1, the first digital potentiometer will set vout, such that Vout = 1.2 + (Rfb * (1.2/500)). The potentiometer has 256 steps of ~39 Ohms, which means that Vout will have 256 steps of 0.093 Volts. But when the device is on (state 2) vout will be set by the second potentiometer such that Vout = 2.4 - Vref_buf. This is because R10 will be equal to R11. For which case, Vref_buf will have less than 256 steps at ~0.013 Volts each. 



![stage3's feedback](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/stage3b.PNG)
