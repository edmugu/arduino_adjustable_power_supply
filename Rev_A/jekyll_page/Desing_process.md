---
title: Design Process
has_children: no
parent: Rev A0
nav_order: 1
---

# Design process
## Use cases
Before we design anything, it is better to set some use cases to come with some characteristics our design must meet.

Input battery

| Use Case   | Voltage [V] | Current [A] | Power [W] | Notes                         |
|------------|-------------|-------------|-----------|-------------------------------|
| AA         | 1.5         | 0.050       | 0.075     | This voltage might be too low |
| 9-Volt     | 9           | 0.111       | N/A       | Forced Power to 1 Watt        |
| CAR        | 12.6        | 0.793       | > 10      |                               |
| Power Bank | 5           | 2.4         | 12        |                               |


Output Use cases


| OUTPUT     | Ideal           | Max            |
|------------|-----------------|----------------|
| Power      | 0.1 Watts       | 11 Watts       |
| Current    | 0.1 Amp         | 1 Amp          |
| Voltage    | 5 Volts         | 23 Volts       |
| LOAD       | 50 Ohms         | NA             |




## Pre-requirements
Now that we have all our use cases (and an ideal use case), we can start defining some requirements for our design. 

Input: 	1.0 Volts to 14 Volts

Output:	0-23 Volts

Power:	< 10 Watts [depending on the battery]

Monitors:
	* Voltage, for all the stages of the regulator
	* Current, for the input and output stages

Controls: 	
* Manual, with the help of a potentiometer
* Automatic, with the help of digital resistors

Communications:
* I2C
* USB COM port (provided by Arduino with the [Firmata library](https://www.arduino.cc/en/reference/firmata) )

Versions:
* stand-alone
* Arduino addon



## Design Procedure
### (1) Battery Current Monitor stage
The input batteries used might have a current limit (i.e., the maximum current will be 2.4 Amps as the typical use case). This will be done to ensure the life of the battery. The first step will be to measure the current going into the device. This can be done with a current monitor with a voltage range from 0 to 14V and can detect <2.4 Amps through a sense resistor. The INA199 meets the voltage range requirement, and it has an x200 gain.
R_Sense should be less than 1 ohm since it will have up to 1 Amp going through it. However, it should be high enough to detect the voltage drop. Therefore, we installed a 100mOhm sense resistor with four terminals. We could have picked a smaller resistor, but we stuck with that value since a cheap Arduino will most likely read this. Further, to avoid measuring the voltage drop across the solder pads, we installed a four-terminal resistor.

|        | Voltage      | Notes                     |
| ------ | ------------ | ------------------------- |
| Input  | -0.3 to 26 V |                           |
| Output | Vin - 0.24 V | worse case @ I = 2.4 Amps |

![Schematics of the current monitor](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/Current_monitor.PNG "Current Monitor")


### (2) Step-Up stage
Instead of using an expensive step-down/step-up converter to do all we need, we opted for a cheap two-stage module. We first need to step up the voltage above the maximum output voltage [ to account for inefficiencies]. That way, we can take any battery as the input, no matter its voltage. The IC **LMR64010** will be used for this module. Its maximum output voltage is 40V, which is well above the wanted 23V output. Therefore, its power output is 40 Watts when the regulator is set to output 40 Volts. However, the battery can limit this stage if the battery cannot deliver 40 Watts. Further, this IC has the disadvantage of only taking voltages from 2.7V to 14V. Hence, we can update our requirements only to take voltages as low as 2.7 Volts.

|        | Voltage     | Current | Notes           |
| ------ | ----------- | ------- | --------------- |
| Input  | 2.7 to 14 V |         |                 |
| Output | <40 V       | <1 A    | ~85% efficiency |

![Schematics of the Step-Up stage](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/Step_up.PNG "Step-Up stage")


### (3) Step-Down stage

#### (3A) Step-Down switch substage
The previous stage will output a voltage of up to 40 Volts. However, the final output needs to be above 23 Volts. The IC **AOZ1282CI** is a cheap buck converter that takes up to 36 Volts. It can reduce the voltage from 0.8 V to 85% of the input voltage. If I want to output 23 Volts, I need at least [Vout = 0.85 Vin OR Vin = 23/.85] 27 Volts. Hence, 36 Volts is good enough to give me some wiggle room. Note that output voltage should be slightly higher than the final output voltage to count for inefficiencies in the next stage. Therefore, the feedback circuit has to feed on the next substage. Further, I can keep this stage to the maximum voltage needed of 27 Volts [ + some wiggle room].

|        | Voltage        | Current | Notes           |
| ------ | -------------- | ------- | --------------- |
| Input  | 4.5 to 36 V    |         |                 |
| Output | 0.8 to 85% Vin | <1.2 A  | efficiency >85% |


![Schematics of the Step-Down Switch](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/Step_down_switch.PNG "Step-Down switch")

#### (3B) Step-Down Linear Regulator substage

The second substage is used to clean any noise created on the step-down switch. Now the **LM317** is an adjustable linear regulator that can output over 1 Amp and take in up to 40 Volts. This meets our needs effectively.

|        | Voltage          | Current |
| ------ | ---------------- | ------- |
| Input  | 4.25 to 40 Volts |         |
| Output | 1.25 to 37 Volts | <1.5 A  |

![Schematics of the Step-Down linear regulator](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/Step_down_linear.PNG "Step-Down linear regulator")

#### (3C) Feedback to substages

The main challenge is that the first substage's voltage should be above the output of the second substage. However, if the difference in the voltage between the two is too high, the second stage will have to "overburn" the excess voltage, making it less efficient. On top of that, the final voltage is adjustable. To tackle this, an operational amplifier is used to calculate the voltage difference between the stages. This voltage will be fed to the second stage [the switching regulator], which will raise its voltage until its feedback reaches its critical voltage. Hence, the voltage of the switching regulator will be held above the final output.

![Schematics of the feedback circuit](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/step_down_feedback.PNG "feedback circuit")


### (4) Final Battery Current Monitor stage

This is the final stage of the power supply. By having a current monitor at the beginning and the end, we can calculate the power supply's efficiency. Also, the feedback voltage of the previous stage takes the drop across this stage by feeding the "final" voltage to the linear regulator. 

### (5) Arduino Control 

 To make the design controllable by an Arduino, an I2C digital pot was added to one of the choose-able feedback circuits. 



![regulator_feedback](https://raw.githubusercontent.com/edmugu/arduino_adjustable_power_supply/master/documentation/snippets/regulator_feedback.PNG)


## Test validation

To guarantee that the board works and can be massed produced, some basic validation tests have to be set. These should include software and hardware test, [which are described on the wiki with more details](https://github.com/edmugu/arduino_adjustable_power_supply/wiki/Hardware-Test-procedure)

