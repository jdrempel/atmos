#!/usr/local/bin/python3.8

# connections.py
# Contains classes and utility functions related to the operation of serial communication
# between ATMOS and the MCU (connected via COM port)

import serial as ser
from base64 import b64decode, b64encode
from time import monotonic, sleep
from typing import Union


class SerialLock:
    """
    Prevents a SerialLine instance from being read/written for a duration of time
    """

    def __init__(self):
        """
        Initializes a new SerialLock instance
        """
        self.duration = 0  # how long before the lock can be attempted
        self.active = False  # whether the lock is currently locked
        self.time = 0  # the time at which the lock was locked
        self.key = (
            None  # a base64 byte sequence that must be provided to unlock this lock
        )

    def attempt_unlock(self, key: Union[int, float, str, bytes] = None) -> bool:
        """
        Attempts to unlock this SerialLock instance

        :param key: (optional) A string or other sequence that is use to unlock
        :type key: Union[int, float, str, bytes]
        :return: Whether the lock is now UN-locked
        :rtype: bool
        """
        if not self.active:  # cover the case where the lock is already unlocked
            return True
        if monotonic() - self.time >= self.duration:
            if self.key is None:  # cover the case where there is no key
                self.active = False
                return True
            decoded_key = b64decode(self.key)
            if decoded_key == bytes(str(key), "utf-8"):
                self.active = False
        return not self.active

    def lock(self, duration: int, key: Union[int, float, str, bytes] = None) -> None:
        """
        Locks this SerialLock instance

        :param duration: The amount of time in seconds that this lock is in effect
        :type duration: int
        :param key: (optional) A string or other sequence that is used to unlock
        :type key: Union[int, float, str, bytes]
        """
        self.duration = duration
        self.key = (
            b64encode(bytes(str(key), "utf-8")) if key is not None else key
        )  # I hate Python ternary
        self.time = monotonic()
        self.active = True


def locked(func):
    """
    A decorator to ensure that a SerialLine method abides by SerialLock protocols

    :param func: The function being decorated
    :type func: callable
    :return: The decorated function
    :rtype: callable
    """

    def decorator(self, *args, **kwargs):
        """
        A decorator to ensure that a SerialLine method abides by SerialLock protocols

        :param self: The class instance whose method is being decorated
        :type self: object
        :return: The result of the decorated function
        :rtype: Any
        """

        lock = getattr(self, "lock", None)
        if lock is None:
            return
        key = getattr(self, "key", None)
        result = None
        if lock.attempt_unlock(key):
            result = func(self, *args, **kwargs)
        return result

    return decorator


class SerialLine:
    """
    Provides a restricted Serial object for use in ATMOS Test instances
    """

    def __init__(self, name, port, baud, **options):
        """
        Initializes a new SerialLine instance
        IMPORTANT: The Serial line will be opened automatically and then immediately closed
                   This is an artifact of how pySerial initializes its Serial instances and
                   is subject to change in future versions (it should not break compatibility)
        """

        self.name = name
        self.port = port
        self.baud = baud
        self.lock = SerialLock()
        self.key = f"{monotonic()}"

        self.byte_size = options.get("byte_size", ser.EIGHTBITS)
        self.parity = options.get("parity", ser.PARITY_NONE)
        self.stop_bits = options.get("stop_bits", ser.STOPBITS_ONE)
        self.timeout = options.get("timeout", 10)

        self._line = ser.Serial(
            port=self.port,
            baudrate=self.baud,
            bytesize=self.byte_size,
            parity=self.parity,
            stopbits=self.stop_bits,
            timeout=self.timeout,
        )
        self._line.close()

    def open(self):
        """
        Opens and subsequently locks the serial line for 2 seconds (to give it time to open)
        """
        self._line.open()
        self.lock.lock(2, self.key)

    def close(self):
        """
        Closes the serial line immediately
        """
        self._line.close()

    @property
    def is_open(self):
        """
        Determines whether the serial line is currently open

        :return: True if the line is open, False otherwise
        :rtype: bool
        """
        return self._line.is_open

    @locked
    def transmit(self, message: bytes):
        """
        Writes data to the serial line

        :param message: The raw data to be written to the serial port
        :type message: bytes
        :return: The number of bytes written
        :rtype: int
        """
        return self._line.write(message)

    @locked
    def receive(self):
        """
        Reads data from the serial line until a terminator is received

        :return: The data received from the line
        :rtype: bytes
        """
        return self._line.read_until()  # default terminator is linefeed (LF) char

    def __del__(self):
        """
        Cleans up the Serial instance before finalizing the deletion of this SerialLine instance
        """
        if self._line.is_open:
            self._line.close()


if __name__ == "__main__":
    """
    Simple regression test
    """

    class TestClass:
        key = monotonic()

        def __init__(self):
            self.key = TestClass.key
            self.lock = SerialLock()
            self.lock.lock(1.5, self.key)
            print(self.key)

        @locked
        def foo(self, other, world):
            print(f"Hello, {world}! ({other})")

    # myserial = SerialLine('i2c', '/dev/ttyS0', 9600)
    # myserial.open()
    # print(myserial.name, myserial.is_open)
    # del myserial

    t = TestClass()
    for _ in range(10):
        t.foo("Nice", "mundo")
        sleep(0.2)

    t.foo("Hey!", "monday")

    # key = f"{monotonic()}"
    # lock = SerialLock()
    # lock.lock(1, key)

    # key2 = f"{monotonic()}"
    # lock.attempt_unlock(key)
    # lock.attempt_unlock(key2)

    # sleep(1)

    # lock.attempt_unlock(key2)
    # lock.attempt_unlock(str(monotonic()))

    # lock.attempt_unlock(key)
