# test_module.py
# Contains the main classes related to Test mode (i.e. communicating with MCU via COM port)

from abc import ABC, abstractmethod
from typing import Any, Union

# from .connections import SerialLine

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
        # self.connection = SerialLine(f"Serial-{self.__class__.__name__}", "/dev/ttyUSB0", 9600)
        # self.connection.open()  # TODO: Lock the line for at least a second before allowing any tx

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

    def tx(self, message):  # TODO: Add type hints
        """
        Transmits a message via the serial line to the MCU

        :param message: The message to be sent (TODO: What format?)
        :type message: TODO: What type?
        :return: TODO: What?
        :rtype: TODO: What type is the returned value?
        """
        pass

    def rx(self, timeout: int):  # TODO: Add type hints
        """
        Polls for a message from the MCU on the serial line

        :param timeout: The amount of time in milliseconds to wait for the signal
        :type timout: int
        :return: The message that was received from the MCU
        :rtype: TODO: What format?
        """
        pass

    def to_bytes(self, x: Union[str, Union[int, float]]) -> bytes:
        """
        A wrapper for converting some data to bytes for serial transmission

        :param x: The data to be converted
        :type x: Any
        :return: The data as a byte sequence
        :rtype: bytes
        """
        return bytes(x, "utf-8")

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Contains the instructions to be executed as part of the test routine

        :return: True if the test executes without any exceptions, False otherwise
        :rtype: bool
        """
        return NotImplementedError(
            "Test.execute() is an abstract method and must be overridden."
        )
