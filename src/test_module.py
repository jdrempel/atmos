# test_module.py
# Contains the main classes related to Test mode (i.e. communicating with MCU via COM port)

from os.path import *

from connections import SerialLine

"""
TEST MODE
---------

Allows the user to transmit predefined driver signals to the MCU to be passed on to the
unit-under-test (UUT). The test consists of a series of plain-text commands which form a
language grammar that is then parsed into Python pseudo-instructions and transmitted to
the MCU to be executed as signals on a serial connection.
"""


class Test():
    """
    Manages the state and properties of a test
    """

    def __init__(self):
        pass

    def _import(self, location: str) -> bool:
        """
        Loads the contents of a file to be interpreted as a test

        :param location: The path (absolute or relative) to the desired input file
        :type location: str
        :return: True if the file exists and the load is successful, False otherwise
        :rtype: bool
        """
        pass

    def run(self) -> None:
        """
        Begins the test and iterates through all operations
        """
        pass

    def check_connection(self) -> bool:
        """
        Confirms a good connection with the MCU

        :return: True if a handshake signal sent to the MCU is acknowledged, False otherwise
        :rtype: bool
        """
        pass

    def export(self, location: str) -> bool:
        """
        Saves the results of the test operation to a file

        :param location: The path (absolute or relative) to the desired output file
        :type location: str
        :return: True if the export operation was successful, False otherwise
        :rtype: bool
        """
        pass
