#!/home/jeremy/Envs/atmos/bin/python

# atmos.py
# Contains the entrypoint for the ATMOS software

from menu import App, TerminalMenu
from ui import Prompt, TUI

# Change me if using a different menu type (default is TerminalMenu)
MENU_TYPE = TerminalMenu

class WelcomeScreen(MENU_TYPE):
    """ 
    The first menu (select mode)
    """ 
    
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

    def perform(self, data):
        if data == 1:
            self.next = self.prev
        elif data == 9:
            self.app_event("EXIT")
        elif data == 0:
            self.next = self.lookup_menu("WelcomeScreen")

class SimMenu(MENU_TYPE):
    """
    The simulation main menu
    """

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
        1: "1. Test",
        2: "2. Simulation",
        3: "3. Mission Ops",
        9: "9. Exit",
    }

    # Navigation menu prompt
    nav_select = {
        1: "1. Back",
        9: "9. Exit",
        0: "0. Home",
    }

    # Main menu (mode select)
    mode_prompt = Prompt("Select one of the following options:", int, mode_select)
    welcome = WelcomeScreen(welcome_msg, mode_prompt)

    # Test menu
    test_prompt = Prompt("Where to next?", int, nav_select)
    test = TestMenu("---- TEST ----", test_prompt)

    # Simulation menu
    sim_prompt = Prompt("Where to next?", int, nav_select)
    sim = SimMenu("---- SIM ----", sim_prompt)

    # Mission Ops menu
    mos_prompt = Prompt("Where to next?", int, nav_select)
    mos = MissionOpsMenu("---- MISSION OPS ----", mos_prompt)

    app = App.instance()
    app.run(welcome)
