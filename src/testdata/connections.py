# connections.py
# Contains classes and utility functions related to the operation of serial communication
# between ATMOS and the MCU (connected via COM port)

import serial as ser


class SerialLine:

    def __init__(self, name, port, baud, **options):
        self.name = name
        self.port = port
        self.baud = baud

        try:
            self.byte_size = options['byte_size']
        except KeyError:
            self.byte_size = ser.EIGHTBITS
        
        try:
            self.parity = options['parity']
        except KeyError:
            self.parity = ser.PARITY_NONE
        
        try:
            self.stop_bits = options['stop_bits']
        except KeyError:
            self.stop_bits = ser.STOPBITS_ONE
        
        try:
            self.timeout = options['timeout']
        except KeyError:
            self.timeout = None

        self._line = ser.Serial(
            port=self.port,
            baudrate=self.baud,
            bytesize=self.byte_size,
            parity=self.parity,
            stopbits=self.stop_bits,
            timeout=self.timeout
        )
        self._line.close()
    
    def open(self):
        self._line.open()
    
    @property
    def is_open(self):
        return self._line.is_open
    
    def __del__(self):
        if self._line.is_open:
            self._line.close()


if __name__ == '__main__':
    myserial = SerialLine('i2c', '/dev/ttyS0', 9600)
    myserial.open()
    print(myserial.name, myserial.is_open)
    del myserial