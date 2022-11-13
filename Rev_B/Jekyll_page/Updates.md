---
layout: default
title: Rev. B Updates
nav_order: 1
parent: Rev B0
---

# Simulation Updates

For this revision, there have been more simulations for all the subcircuits. And to guarantee real-life performance, I decided to use LTspice, the simulator from "Analog Devices"/"Linear Technologies." They already have proper models for their device portfolio, so it would not be so hard to use this for this project. 

# Hardware Updates

## (1) Regulators vs. Controllers

After debugging Rev. A, I noted that at the moment, there was no IC sold in Digi key that could output over >= 2 amps **with the same package**.  That is when I realized that voltage controllers are more upgradeable than voltage regulators. The reason is that a voltage regulator is a voltage controller WITH a power transistor and current sense mechanism. So if you want to upgrade your voltage controller power supply to handle more power, you have to update the power transistor and current sense mechanism. And if you want to upgrade a voltage regulator, you hope there is an IC with the same package that meets your requirements. 

Also, while designing Rev A, I did not realize that the final linear voltage regular used **LM317** is very inefficient. It requires at least a 3-volts difference between the input and the output. That is when I can with the **MIC5157** voltage controller. 

## (2) Reverse Voltage Protection

This is something that was not included on Rev. A at all, and it is important. 

## (3) Minimum voltage output

The minimum voltage output most voltage regulators can output is its internal reference voltage level. So most regulators can't go below 1.2 Volts by themselves. And this bothers me since the reference design from Linear Technologies can be to 0 volts. Then I found this article from Texas Instruments on how to tackle this issue which is [linked here](https://github.com/edmugu/arduino_adjustable_power_supply/blob/master/documentation/TI_Below_1V2.pdf) .  The article derives the equation shown below. 
$$
Vout = V_{REFint} * (1+ \frac {R_{TOP}}{R_{BOT}}) - (\frac{R_{TOP}}{R_{BOT}}*V_{REFext})
$$
The plan would be to operate Vout normally when Vout > 2.4 Volts. But for Vout < 2.4 the Vrefext would be used to adjust the voltage instead of the resistor ratio. That scenario leads to the following equation: 


$$
Vout = V_{REFint} * 2 - V_{REFext}
$$
which practically means that the average of Vout and Vrefext has to be 1.2Volts


$$
\frac{Vout+V_{REFext}}{2} = V_{REFint} = 1.2 [volts]
$$


So if one varies Vref from 0 to 2.4 Volts it will vary Vout from 2.4 to 0 volts. 



## (4) Trigger/Soft-starter

To add a trigger and soft start, I wanted to add a tap that would control Vrefext. But to make it easier for the user this tap would take an input between 0 and 1 volt to represent 0% to 100% of the voltage set.  That would leave to the following equation where k is pre-gain on the Vtap. 

$$
Vout = V_{REFint} * (1+ \frac {R_{TOP}}{R_{BOT}}) - (\frac{R_{TOP}}{R_{BOT}}*k*V_{tap})
$$
So to simplify the equation, 




$$
Vref*(1 + \frac{R_{TOP}}{R_{BOT}} )= \frac{R_{TOP}}{R_{BOT}} * k
$$
if we solve for k




$$
k = Vref * (\frac{R_{BOT}}{R_{TOP}} + 1)
$$



## (5) Sense ports

Sense ports were added to take into account the voltage drop on the wires. 
