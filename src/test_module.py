#!/home/jeremy/Envs/atmos/bin/python
# Commands for a test file:
# start                 -- marks the beginning of a test
# stop                  -- marks the end of a test
# wait <ms>             -- remain inactive (no tx/rx or other actions) for <ms> milliseconds
# tx <line> <signal>    -- transmits <signal> on bus/wire <line>
# rx <line> <timeout>   -- waits for a response on bus/wire <line> for <timeout> milliseconds
# disp <buffer>         -- prints the contents of <buffer> (associated with a line)
# 
# Control flow:
# for <iter> = <1st>:<step>:<end> / endfor                    -- creates / ends a for loop block
# while <line or iter> lt/gt/eq/neq/gte/lte / endwhile        -- creates / ends a while loop block
# 
# EXAMPLE.tst
# -----------
# start
# wait 5000
# tx iic 0x1f
# wait 50
# rx iic
# disp iic
# stop

from os.path import *
from queue import LifoQueue as Stack
from queue import Queue
from time import sleep

from command import Command
from connections import *


class RunTest(Command):
    """
    Begins the execution of a test
    """

    def execute(self):
        print("Executing!")


def test_log_output(widget, *outputs):
    for output in outputs:
        widget.values.append(output)
        # widget.update(clear=False)
        widget.display()


def load_testfile(path):
    """
    Loads the test file and splits it into individual lines

    :param path: A string or path-like object containing a relative or absolute path to the file
    :type path: str
    :return: A list of the lines from the test file
    :rtype: list[str]
    """

    assert isinstance(path, str), "Parameter path must be a string"

    abs_path = abspath(path)
    with open(abs_path, 'r') as test_file:
        lines = test_file.readlines()

    return lines


def h_start(widget, ):
    
    test_log_output(widget, "Starting the test!")

    return True


def h_stop(widget, ):

    test_log_output(widget, "Stopping the test!")

    return True


def h_wait(widget, millis):

    millis = abs(round(millis))
    seconds = millis/1000
    sleep(seconds)

    return True


def h_tx(widget, line, data):

    test_log_output(widget, f"Transmitting {data} on line {line}!")

    return True


def h_rx(widget, line, timeout):

    test_log_output(widget, f"Receiving on line {line}...")
    millis = abs(round(timeout))
    seconds = millis/1000
    sleep(seconds)
    test_log_output(widget, f"Waited {millis} ms and timed out!")

    return True


def h_disp(widget, buffer):

    test_log_output(widget, f"{buffer} contents HERE")

    return True


def parse_testfile(widget, lines):

    assert isinstance(lines, list), "Parameter lines must be a list"

    line_queue = Queue(0)

    action_queue = Queue(0)

    for line in lines:
        line_queue.put(line)
    
    while not line_queue.empty():
        next_line = line_queue.get()
        words = next_line.split()

        if not words:
            continue

        if words[0] == 'start':
            action_queue.put([h_start,])

        elif words[0] == 'stop':
            action_queue.put([h_stop,])

        elif words[0] == 'wait':
            millis = int(words[1])
            action_queue.put([h_wait, millis])

        elif words[0] == 'tx':
            line = words[1]
            data = hex(int(words[2], 16))
            action_queue.put([h_tx, line, data])

        elif words[0] == 'rx':
            line = words[1]
            timeout = int(words[2])
            action_queue.put([h_rx, line, timeout])

        elif words[0] == 'disp':
            buffer = words[1]
            action_queue.put([h_disp, buffer])

        elif words[0] == 'for':
            pass  # ENTER A FOR LOOP

        elif words[0] == 'while':
            pass  # ENTER A WHILE LOOP
    
    widget.values = []
    widget.update(clear=True)
    
    while not action_queue.empty():
        next_action = action_queue.get()
        function = next_action[0]
        if len(next_action) > 1:
            args = [widget,] + next_action[1:]
        else:
            args = [widget,]
        status = function(*args)


if __name__ == "__main__":
    lines = load_testfile('./test/test.txt')
    parse_testfile(lines)