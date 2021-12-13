# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 2021

Controls the board.

EXAMPLE: 
        python board.py --port=COM3 read_voltage
        python board.py --port=COM3 read_current
        python board.py --port=COM3 calculate_load --verbose=False


REQUIREMENTS:
    python 3.7+
    pyfirmata  (to talk to the arduino)
    fire (to create command line tool)

@author: Eduardo Munoz
@email: edmugu@protonmail.com
"""
import pyfirmata
import fire
import time


class Board(object):
    """
    It controls the Arduino_Adjustable_Power_Supply module
    """

    log = ""
    version = "0.1"
    arduino_vcc = 5.0
    read_retries = 9  # The firmata library sometimes needs to reread analog voltage

    v_to_i = 1.0 / (100 * 0.1)
    power = {"in": None, "out": None}
    pins = [
        {"num": 0, "name": "Iin", "scale": v_to_i, "cur_pin": True, "value": None},
        {"num": 1, "name": "Vin", "scale": 4.56, "cur_pin": False, "value": None},
        {"num": 2, "name": "Vup", "scale": 13.74, "cur_pin": False, "value": None},
        {"num": 3, "name": "Vout", "scale": 13.74, "cur_pin": False, "value": None},
        {"num": 4, "name": "Iout", "scale": v_to_i, "cur_pin": True, "value": None},
        {"num": 5, "name": "Vdown", "scale": 31.09, "cur_pin": False, "value": None},
    ]

    def __init__(self, port="COM3"):
        print("\nboard.py version %s" % self.version)
        self.board = pyfirmata.Arduino(port)
        print("the board's firmware is version %s.%s" % self.board.firmware_version)

        # Enabling the IO
        it = pyfirmata.util.Iterator(self.board)
        it.start()
        for p in self.pins:
            self.board.analog[p["num"]].enable_reporting()
        time.sleep(0.1)

    def print(self, msg, verbose=True):
        self.log += "\n" + msg
        if verbose:
            print(msg)

    def print_lot(self):
        print(self.log)

    def read_voltage(self, verbose=True):
        """
        It reads the voltage of all the stages of the unit
        """
        self.print("reading the raw voltages\n", verbose)
        for p in filter(lambda x: x["cur_pin"] == False, self.pins):
            p["value"] = self.board.analog[p["num"]].read()
            for _ in range(self.read_retries):
                if p["value"] is not None:
                    vcc_percent = p["value"] * 100
                    p["value"] = p["value"] * self.arduino_vcc
                    self.print(
                        "Read %#04.1f%% of VCC on pin a%s (= %3.2f Volts)"
                        % (vcc_percent, p["num"], p["value"]),
                        verbose,
                    )
                    break
            if p["value"] is None:
                self.print(
                    "Read NONE on pin a%s [this might be a bug on the board's FW. run again]"
                    % p,
                    verbose,
                )
        self.print("\nCalculating the voltages on the board", verbose)
        for p in filter(lambda x: x["cur_pin"] == False, self.pins):
            if p["value"] is not None:
                p["value"] = p["value"] * p["scale"]
                self.print("%9s is %#05.2f Volts" % (p["name"], p["value"]), verbose)

    def read_current(self, verbose=True):
        """
        It reads the current going in and out
        """
        self.print("reading the raw voltages\n", verbose)
        for p in filter(lambda x: x["cur_pin"] == True, self.pins):
            p["value"] = self.board.analog[p["num"]].read()
            for _ in range(self.read_retries):
                if p["value"] is not None:
                    vcc_percent = p["value"] * 100
                    p["value"] = p["value"] * self.arduino_vcc
                    s = "Read %#04.1f%% of VCC on pin a%s (= %3.2f Volts)" % (
                        vcc_percent,
                        p["num"],
                        p["value"],
                    )
                    self.print(s, verbose)
                    break
            if p["value"] is None:
                self.print(
                    "Read NONE on pin a%s [this might be a bug on the board's FW. run again]"
                    % p,
                    verbose,
                )

        self.print("\nCalculating the voltages on the board", verbose)
        for p in filter(lambda x: x["cur_pin"] == True, self.pins):
            if p["value"] is not None:
                p["value"] = p["value"] * p["scale"]
                self.print(
                    "%9s is %#07.2f miliAmps" % (p["name"], p["value"] * 1000), verbose
                )

    def calculate_load(self, verbose=True):
        self.read_voltage(verbose=False)
        self.read_current(verbose=False)
        self.print("Calculating the load on the output\n", verbose)

        pvout = list(filter(lambda x: x["name"] == "Vout", self.pins))[0]["value"]
        piout = list(filter(lambda x: x["name"] == "Iout", self.pins))[0]["value"]

        if (pvout is None) or (piout is None):
            self.print("had issues reading voltage or current", verbose)
            return
        ans = pvout / piout
        self.print("Rload is %05.2f\n" % ans, verbose)

    def calculate_power(self, read_tries=99):
        self.calculate_load(verbose=False)
        vin = list(filter(lambda x: x["name"] == "Vin", self.pins))[0]["value"]
        iin = list(filter(lambda x: x["name"] == "Iin", self.pins))[0]["value"]
        vout = list(filter(lambda x: x["name"] == "Vout", self.pins))[0]["value"]
        iout = list(filter(lambda x: x["name"] == "Iout", self.pins))[0]["value"]

        self.power["in"] = vin * iin
        self.power["out"] = vout * iout

        self.print("Power in : %7.3f Watts" % self.power["in"])
        self.print("Power out: %7.3f Watts" % self.power["out"])

    def calculate_efficiency(self, read_tries=99):
        self.calculate_power()
        efficiency = self.power["out"] / self.power["in"]
        self.print("Efficiency: %4.1f %% " % efficiency)


if __name__ == "__main__":
    fire.Fire(Board)
