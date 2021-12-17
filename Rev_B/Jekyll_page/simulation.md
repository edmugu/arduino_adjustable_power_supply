---
layout: default
title: Simulation
nav_order: 3
parent: Rev. B
---

# Intro to Simulation study 

In short, I have learned that to design a power circuit right you have to use the SPICE tools of the PROs[i.e. Texas Instruments and Analog Devices]. Their tools will have the proper model for the components they sell and the supporting components they used to test their devices. So their SPICE simulations will be far better than the ones and average engineer can do by importing models or making pseudo models of the components they plan to use. With that out the way, the following are the simulations I have done and the "learning nuggets" I have come across. Also while simulating this, it appear that the output requirements seem to be driving this most of the time, so I will start with the output stage and go backwards through the design. 



# Stage 3: Linear Regulator Controller

This is the last stage [besides the reverse current protection] and it is probably the most complicated part of the design. But the bottom line is that this stage will burn off some of buck converter output and will leave a clean output on Vout. But to achieve that, the controller, ideally, will require two Voltage inputs. Vboost will drive the controller logic and has to be at least 2 Volts above Vout so it can drive the MOSFET properly. However, Vbuck will deliver all the power going to Vout and has to be close to Vout so that the MOSFET does not have to work as hard, burning off the unwanted voltage. This is shown on the image below. 

![Stage3](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev_B/Jekyll_page/snipits/stage3a.PNG )

