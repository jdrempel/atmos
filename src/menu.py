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
        self.prompt = prompt
        self._prev = None
        self._next = None
        self._callback = callback
        self._app = None

    def display(self) -> None:
        """
        Displays the menu via the applicable UI
        """
        self.interface.output(self.message)
        response = None
        if self.prompt is not None:
            response = self.interface.prompt(self.prompt)
        try:
            self._callback(response)
        except TypeError:
            pass
        self.perform(response)

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
    
    def set_app(self, app) -> None:
        """ 
        Sets the app that this menu belongs to

        :param app: The app to which this menu belongs
        :type app: App
        """ 
        self._app = app
    
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
    
class TerminalMenu(BaseMenu):
    """ 
    Implements a terminal UI menu (text-based)
    """ 

    def __init__(self, message: str, prompt: Prompt, callback=None):
        super().__init__(message, prompt, callback)
        self.interface = TUI()
    
    @abstractmethod
    def perform(self) -> None:
        pass
    
class App:
    """ 
    Manages the state of the application and transitions between menus
    """ 

    def __init__(self, menus: list, start: BaseMenu):
        """
        Instantiates a new App

        :param menus: A list of the menus belonging to this App
        :type menus: list
        :param start: The menu at which the App starts
        :type start: BaseMenu
        """
        self.current_menu = start
        self.previous_menu = None
        self.next_menu = None
        self.menus = menus
        self.running = True

        for menu in menus:
            menu.set_app(self)
    
    def run(self):
        while self.running:
            self.current_menu.display()
    
    def go_next(self):
        self.previous_menu = self.current_menu
        self.current_menu = self.next_menu
        self.next_menu = self.current_menu.next
        self.current_menu.display()
    
    def go_back(self):
        self.next_menu = self.current_menu
        self.current_menu = self.previous_menu
        self.previous_menu = self.current_menu.prev
        self.current_menu.display()
    
    def listen(self, message):
        if message == "EXIT":
            self.running = False
