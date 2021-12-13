---
title: Intro
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---


# [Arduino Power Supply](https://edmugu.github.io/arduino_adjustable_power_supply/)

![3d view of pcb file](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/3d%20view.PNG "Power Supply")

## Abstract

This project is based on the [LT journal's Article from Keith Szolusha](https://github.com/edmugu/arduino_portable_adjustable_power_supply/blob/master/documentation/LTJournal-Bench_Supply.pdf). In the article, he discussed how to design a clean power supply. However, this design is augmented by making it controllable by an Arduino. Use Cases Include motor controller, high power wireless communication, and benchtop supply.


## Intro

On the original design by Szolusha, there are four modules. (1) a switching regulator that steps down a 10-40V input to an intermediate voltage that is slightly above the output voltage. (2) Linear regulator that "cleans" the output. (3) The current source sets a reference voltage that is not affected by temperature. Lastly, (4) A current sink that helps the Linear regulator reach low voltages.

We will modify each block to fit our needs, making this portable and usable with any common household batteries. So the base design is shown on the diagram below. The first step is to step up the battery's voltage to a usable voltage we can step down. The second step is to step down the voltage to the wanted voltages like 3.3 Volts, 5.0 Volts, and Vout. However, the efficient step-down switches can create "switching ripples" on the output. These ripples aren't a big deal; however, one could use an inefficient LDO regulator if one needs a very clean supply. So will use the step-down switch and regulator to create a clean semi-efficient voltage output as shown on the diagram.

![logic schematics](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/Arduino-power-supply.png "logic schematics")

The main target battery is a USB power bank. Most USB power banks can deliver 12W @ 5Volts. Hence, this power supply will deliver 10 Watts at its output to accommodate the inefficiencies of the power stages of this design. Since the default use case will power a 50-ohm load, the maximum voltage at the output should be greater than 22.36 Volts to deliver 10 Watts.

