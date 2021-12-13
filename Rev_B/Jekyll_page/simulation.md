---
layout: default
title: Simulation
nav_order: 3
parent: Rev. B
---

# Stage 0: Reverse Voltage Protection

For this module, we are going to use IC **LTC4367** with a **IRF6644** MOSFET. 

- Typical load:   This will represent the ideal case scenario of 5 Volts @ 2.1 Amps going in.

- Reverse Voltage: The max voltage battery [of 12 volts] is hooked backward.

- Max Current:  2.1 Amps \[1\]

  



We need to set the voltage limits. For OV and UV, 25V and 3V were selected. This gives us the following formulas: 

(1) 25 * R3 / (R1 + R2 + R3) = 0.5

(2) 3 *  (R3 + R2) / (R1+R2+R3) = 0.5

(3) R1 + R2 + R3 = 100k

This gives us R1 = 83.3k, R2 = 14.6k, R3 = 2k

# Stage 1: Step-up Voltage controller

For this module, we are going to use IC **LT3757** 

### UV limit

We need to set UV voltage limit of 1.22 Volts. 

1.22 = 3.0 * (R1) / (R1 + R2)

R1 = 20k  and R2 = 13.7k

### FeedBack

We need to output 36Volts on this stage. 

1.6V = 36 R1 / (R1 + R2)

R1 = 21k, R2 = 1k

### Inductor

From simulations we can see that a 10uH will do the job. 

### Rsense

We need to set the 2.1 Amp limit on the output. 

0.108 = Rsense * 2.1

Rsense = 51 mOhms



### Simulation Results

On the first plot, one can see the input current [ Ix] and the output current [Iload]. The "stage 1" does limit the input current to below 2.1 Amps. And it is able to supply the 0.5 amps requested [ 0.5 Amps * 36 Volts = 18 Watts].

On the second plot and third plot, one can see the output voltage [vout] and the voltage created by the inductor [nmos_drain]. This stage can set the right voltage output and stop charging the inductor after meeting the desired voltage. 

![Stage 1 simulation](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/Rev.%20B/Simulation/snip-it/stage_1_max_current.PNG)



# Stage 2: Step-down Voltage controller

For this module, we are going to use IC **LTC7803** 

Rsense = Vsense_max/ (I_max + Delta_I / 2)  where Vsense_max = 50mV

if we ignore Detal_I for a moment, one can see that Rsense < 50mV / I_max. 

Rsense_aprox = 50mV / 0.5 Amps = 100mOhms

