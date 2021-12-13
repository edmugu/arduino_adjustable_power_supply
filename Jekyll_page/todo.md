---
title: Todo
has_children: no
nav_order: 50
parent:Rev. A
---





* Before Next Hardware revision
  * check the firmata's i2c support on https://mryslab.github.io/pymata4/ 

* Must have fixes on the Next Hardware revision
  * Fix the Diode footprint that is backwards
    * Add a jumper to connect the board vin to the Arduino Vin 
  * Add LED lights to indicate 
    * That the voltage levels are good
    * That there is no over-current event
  * Make the module stack-able
    * Add i2c ADC to free the Arduino ADC
    * Add i2c repeater like PCA9515A to control the i2c bus between modules
      * Add i2c eeprom to save some calibration values
        * Replace some capacitor SMA to BIG through hole capacitors 

* Nice to have fixes on the Next Hardware revision
  * Better banana connectors on the output
  * silk layer with more expiation on each stage of the module