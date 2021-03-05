# ui.py
# Handles user input and outputs information to console

from abc import ABC, abstractmethod
from typing import Any, Union


class Prompt:
    """ 
    Represents a text prompt and its anticipated response type
    """ 

    def __init__(self, message, expected_type, options={}):
        self._message = message
        self.type = expected_type
        self._options = options
    
    @property
    def message(self):
        output = self._message
        if len(self._options) > 0:
            output += "\n"
            for k, v in self._options.items():
                output += f"{k}. {v}\n"
        return output

# Class: BaseOutput
# Purpose: Abstract base class for output to user
class BaseOutput(ABC):
    """ 
    Abstract base class for output to user.
    """

    @abstractmethod
    def put(self, output: str) -> None:
        """
        Places a string on the output media.

        :param output: The string to be output
        :type output: str
        """
        pass

# Class: TerminalOutput
# Purpose: Allows text output to a terminal environment
class TerminalOutput(BaseOutput):
    """ 
    Allows text output to a terminal environment.
    """

    def put(self, output: str) -> None:
        """
        Outputs a string to console

        :param output: A string to be displayed
        :type output: str
        """
        print(output)

# Class: BaseInput
# Purpose: Abstract base class for user input
class BaseInput(ABC):
    """ 
    Abstract base class for user input. 
    """

    @abstractmethod
    def get(self) -> str:
        """
        Gets a string from the user interface

        :return: The raw string from the UI
        :rtype: str
        """
        pass

# Class: TerminalInput
# Purpose: Allows text input from a terminal environment
class TerminalInput(BaseInput):
    """
    Allows text input from a terminal environment.
    """

    def get(self) -> str:
        """
        Returns a string as input from the terminal

        :return: The newline-terminated string from the terminal
        :rtype: str
        """
        return input()

# Class: UI
# Purpose: Abstract base class for user interface
class UI(ABC):
    """ 
    Abstract base class for a user interface.
    """ 

    def __init__(self):
        """
        :inputSrc: An object of a type implementing BaseInput

        :outputDst: An object of a type implementing BaseOutput

        :quietMode: If true, suppress warnings to the user
        """
        super().__init__()
        self.inputSrc = None
        self.outputDst = None
        self.quietMode = False

    @abstractmethod
    def get_str(self) -> str:
        """
        Gets a string from the user's input

        :return: The string that the user entered
        :rtype: str
        """
        pass

    @abstractmethod
    def get_num(self) -> Union[int, float]:
        """
        Gets a number from the user's input

        :return: The number that the user entered
        :rtype: Union[int, float]
        """
        pass

    @abstractmethod
    def output(self, string: str) -> None:
        """
        Outputs a string to the output interface

        :param string: The string to be displayed
        :type string: str
        """
        pass

    @abstractmethod
    def prompt(self, prompt: str, type_: Any=str) -> Union[Union[int, float], str]:
        """
        Displays a prompt and waits for user input based on the prompt

        :param prompt: The text to be displayed to the user
        :type prompt: str
        :param type_: The type of the expected input data, defaults to str
        :type type_: Any, optional
        :return: The response from the user (as an int, float, or str)
        :rtype: Union[Union[int, float], str]
        """
        pass

# Class: TUI
# Purpose: User interface in a terminal setting
class TUI(UI):
    """ 
    Implements a user interface (UI) in a terminal setting.
    """

    def __init__(self):
        super().__init__()
        self.outputDst = TerminalOutput()
        self.inputSrc = TerminalInput()

    def get_str(self) -> str:
        """
        Gets a user-entered string from the terminal

        :return: The string the user entered
        :rtype: str
        """
        return self.inputSrc.get()
    
    def get_num(self, any=False) -> Union[int, float]:
        """
        Gets a user-entered number from the terminal

        :param any: (optional) If True, allow this method to return a valid str if the input cannot be converted
        :type any: bool
        :return: The number (int or float) that the user entered
        :rtype: Union[int, float]
        """
        input_str = self.get_str()
        try:
            if float(input_str):
                if int(float(input_str)):
                    return int(float(input_str))
                return float(input_str)
            elif input_str == "0":
                return 0
            else:
                return None
        except ValueError:
            if any == True:
                return input_str
            return None
    
    def output(self, string: str) -> None:
        """
        Outputs a string to the terminal

        :param string: The string to be displayed
        :type string: str
        """
        self.outputDst.put(string)

    def prompt(self, prompt: Prompt):
        """
        Prompts the user and waits for input via the terminal

        :param prompt: The Prompt object to be displayed
        :type prompt: Prompt
        :return: The user's response to the prompt
        :rtype: Union[Union[int, float], str]
        """
        self.output(prompt.message)
        response = None
        if prompt.type == Any:
            response = self.get_num(any=True)  # This could be better-implemented
            try:
                response = int(response)
            except ValueError:
                pass
        elif prompt.type == str:
            response = self.get_str()
        elif prompt.type in [int, float]:
            response = self.get_num()
        return response

