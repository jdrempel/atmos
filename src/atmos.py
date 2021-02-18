#!/usr/local/bin/python3.8

# atmos.py
# Contains the entrypoint for the ATMOS software
from testdata import sample
from menu import App, TerminalMenu
from ui import Prompt, TUI

# Change me if using a different menu type (default is TerminalMenu)
MENU_TYPE = TerminalMenu

class WelcomeScreen(MENU_TYPE):
    """ 
    The first menu (select mode)
    """

    def __init__(self, *args, **kwargs):
        """
        :precond: welcome_msg must exist in the scope immediately outside of this method call
        :type welcome_msg: str
        :precond: mode_select must exist in the scope immediately outside of this method call
        :type mode_select: dict
        """
        super().__init__(*args, **kwargs)
        self.message = welcome_msg
        self.prompt = Prompt(
            "Select one of the following options:",
            int, mode_select
        )
    
    def perform(self, data):
        if data == 1:
            self.next = self.lookup_menu("TestMenu")
        elif data == 2:
            self.next = self.lookup_menu("SimMenu")
        elif data == 3:
            self.next = self.lookup_menu("MissionOpsMenu")
        elif data == 9:
            self.app_event("EXIT")
        else:
            self.app_event("BAD_RESPONSE")

class TestMenu(MENU_TYPE):
    """
    The test main menu
    """

    def __init__(self, *args, **kwargs):
        """
        :precond: test_select must exist in the scope immediately outside of this method call
        :type test_select: dict
        """
        super().__init__(*args, **kwargs)
        self.message = "======== TEST ========"
        self.prompt = Prompt(
            "Select an action:",
            int, test_select
        )

    def perform(self, data):
        if data == 1:
            # Load test
            # self.next = self.lookup_menu("TestLoaderMenu")
            pass
        elif data == 2:
            # Check connection
            # Test.check_connection()
            pass
        elif data == 3:
            # Start test
            test = sample.SampleTest()
            test.run()
            # Test.run()
            pass
        elif data == 4:
            # Export results
            # self.next = self.lookup_menu("TestExportMenu")
            pass
        elif data == 9:
            self.app_event("EXIT")
        elif data == 0:
            self.next = self.lookup_menu("WelcomeScreen")

class SimMenu(MENU_TYPE):
    """
    The simulation main menu
    """

    def __init__(self, *args, **kwargs):
        """
        :precond: nav_select must exist in the scope immediately outside of this method call
        :type nav_select: dict
        """
        super().__init__(*args, **kwargs)
        self.message = "======== SIM ========"
        self.prompt = Prompt(
            "Where to next?",
            int, nav_select
        )

    def perform(self, data):
        if data == 1:
            self.next = self.prev
        elif data == 9:
            self.app_event("EXIT")
        elif data == 0:
            self.next = self.lookup_menu("WelcomeScreen")

class MissionOpsMenu(MENU_TYPE):
    """
    The mission ops main menu
    """

    def __init__(self, *args, **kwargs):
        """
        :precond: nav_select must exist in the scope immediately outside of this method call
        :type nav_select: dict
        """
        super().__init__(*args, **kwargs)
        self.message = "======== MISSION OPS ========"
        self.prompt = Prompt(
            "Where to next?",
            int, nav_select
        )

    def perform(self, data):
        if data == 1:
            self.next = self.prev
        elif data == 9:
            self.app_event("EXIT")
        elif data == 0:
            self.next = self.lookup_menu("WelcomeScreen")

# Application Entrypoint
if __name__ == "__main__":

    welcome_msg = """
======== Welcome to A.T.M.O.S.! ========
[Advance Testing & Mission Ops Software]
----------------------------------------"""
    
    # Mode select menu prompt
    mode_select = {
        1: "Test",
        2: "Simulation",
        3: "Mission Ops",
        9: "Exit",
    }

    # Navigation menu prompt
    nav_select = {
        1: "Back",
        9: "Exit",
        0: "Home",
    }

    # Test mneu prompt
    test_select = {
        1: "Load Test",
        2: "Check Connection",
        3: "Start Test",
        4: "Export Results",
        9: "Exit",
        0: "Home",
    }

    
    welcome = WelcomeScreen() # Main menu (mode select)
    test = TestMenu()   # Test menu
    sim = SimMenu()  # Simulation menu
    mos = MissionOpsMenu()  # Mission Ops menu

    app = App.instance()
    app.run(welcome)
