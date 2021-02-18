# test_module.py
# Contains the main classes related to Test mode (i.e. communicating with MCU via COM port)

from abc import ABC, abstractmethod
from typing import Any

# from connections import SerialLine

"""
TEST MODE
---------

Allows the user to transmit predefined driver signals to the MCU to be passed on to the
unit-under-test (UUT). The test consists of a series of instructions to transmit data to the MCU
over a serial connection.
"""


class Test(ABC):
    """
    Provides an interface for individual tests
    """

    def __init__(self):
        pass

    def _run_full(self, **kwargs) -> None:
        """
        Begins the test and iterates through all operations
        """
        if self._check_connection():
            if self.execute(**kwargs):
                return True
        return False

    def _check_connection(self) -> bool:
        """
        Confirms a good connection with the MCU

        :return: True if a handshake signal sent to the MCU is acknowledged, False otherwise
        :rtype: bool
        """
        return True  # placeholder until normal functionality added

    def _export(self, location: str) -> bool:
        """
        Saves the results of the test operation to a file

        :param location: The path (absolute or relative) to the desired output file
        :type location: str
        :return: True if the export operation was successful, False otherwise
        :rtype: bool
        """
        pass

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Contains the instructions to be executed as part of the test routine

        :return: True if the test executes without any exceptions, False otherwise
        :rtype: bool
        """
        return NotImplementedError("Test.execute() is an abstract method and must be overridden.")