# menu.py
# Handles application state and manages transitions

from abc import ABC, abstractmethod
from typing import Any

from ui import Prompt, TUI

class BaseMenu(ABC):
    """
    Provides an interface for various kinds of menus
    """

    def __init__(self, message:str, prompt:Prompt=None, callback=None):
        self.interface = None
        self.message = message
        self._prompt = prompt
        self._prev = None
        self._next = None
        self._callback = callback
        self._app = App.instance()

        # Register this menu in the App menu registry
        App.register_menu(self)

    def display(self) -> None:
        """
        Displays the menu via the applicable UI
        """
        self.interface.output(self.message)
        response = None
        if self._prompt is not None:
            response = self.interface.prompt(self._prompt)
        try:
            self._callback(response)
        except TypeError:
            pass
        self.perform(response)
    
    @property
    def prompt(self) -> Prompt:
        """
        Returns the prompt (if any) for this menu

        :return: self._prompt
        :rtype: Prompt
        """
        return self._prompt
    
    @prompt.setter
    def prompt(self, prompt: Prompt) -> None:
        """
        Sets the prompt for this menu

        :param prompt: The prompt to be applied to this menu
        :type prompt: Prompt
        """
        self._prompt = prompt

    @property
    def prev(self):
        """
        Returns the menu from which this one came

        :return: The menu previous to this one
        :rtype: BaseMenu
        """
        return self._prev

    @prev.setter
    def prev(self, prev) -> None:
        """
        Sets the menu from which this one came

        :param prev: The menu previous to this one
        :type prev: BaseMenu
        """
        self._prev = prev

    @property
    def next(self):
        """
        Returns the next menu to be displayed

        :return: The menu to follow this one
        :rtype: BaseMenu
        """
        return self._next

    @next.setter
    def next(self, next) -> None:
        """
        Sets the next menu to be displayed

        :param next: The menu to follow this one
        :type next: BaseMenu
        """
        self._next = next
        self._app.load_next(self._next)
    
    def app_event(self, message: Any) -> None:
        """ 
        Sends a message to the menu's app

        :param message: The payload to be delivered to the app
        :type message: Any
        """ 
        self._app.listen(message)
    
    @abstractmethod
    def perform(self, data: Any) -> None:
        """
        Performs the "business logic" for this menu
        """
        pass
    
    def lookup_menu(self, name: str):
        """
        Returns a menu from the current menu's app instance by name

        :param name: The name of the menu to look up
        :type name: str
        """
        return self._app.menus[name]
    
class TerminalMenu(BaseMenu):
    """ 
    Implements a terminal UI menu (text-based)
    """ 

    def __init__(self, message: str, prompt: Prompt=None, callback=None):
        super().__init__(message, prompt, callback)
        self.interface = TUI()
    
    @abstractmethod
    def perform(self) -> None:
        pass

class App:
    """ 
    Manages the state of the application and transitions between menus
    """

    _instance = None
    _menus = {}

    def __init__(self):
        """
        Instantiates a new App (virtual, private constructor)

        :param menus: A list of the menus belonging to this App
        :type menus: list
        :param start: The menu at which the App starts
        :type start: BaseMenu
        """
        if App._instance is not None:
            raise Exception("App instance already exists!")
        App._instance = self

        self.current_menu = None
        self.previous_menu = None
        self.next_menu = None
        self.running = False
    
    @staticmethod
    def instance():
        """
        Static access method
        """
        if App._instance is None:
            App()
        return App._instance
    
    @staticmethod
    def get_menu_name(menu: BaseMenu) -> str:
        """
        Static method for getting the name of a menu class as a string

        :param menu: The menu instance to get the name for
        :type menu: BaseMenu
        :return: The name of the menu's class, in string form
        :rtype: str
        """
        return menu.__class__.__name__
    
    @staticmethod
    def register_menu(menu: BaseMenu) -> None:
        """
        Static method for registering a menu in the app

        :param menu: The menu instance to register
        :type menu: BaseMenu
        """
        App._menus[App.get_menu_name(menu)] = menu
    
    def run(self, start: BaseMenu) -> None:
        """
        The main loop for the application

        :param start: The menu to begin execution from
        :type start: BaseMenu
        """
        self.load_next(start)
        self.running = True
        while self.running:
            self.current_menu.display()
    
    def load_next(self, next: BaseMenu) -> None:
        """
        Updates the state of the application by loading the next menu

        :param next: The next menu to be displayed
        :type next: BaseMenu
        """
        self.previous_menu = self.current_menu
        self.current_menu = next
        self.current_menu.prev = self.previous_menu
    
    def load_prev(self):
        """
        Updates the state of the application by loading the previous menu
        """
        self.next_menu = self.current_menu
        self.current_menu = self.previous_menu
        self.previous_menu = self.current_menu.prev
    
    @property
    def menus(self):
        return self._menus
    
    def listen(self, message: str) -> None:
        """
        Takes action regarding a message from one of the menus

        :param message: A string with information for the app instance to act upon
        :type message: str
        """
        if message == "EXIT":
            self.running = False
        elif message == "BAD_RESPONSE":
            print("ERROR: BadResponse")
            # quit()
