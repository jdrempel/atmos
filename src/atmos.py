#!/home/jeremy/Envs/atmos/bin/python

# atmos.py
# Contains the entrypoint for the ATMOS software

from menu import App, TerminalMenu
from ui import Prompt, TUI

class WelcomeScreen(TerminalMenu):
    """ 
    The first menu (select mode)
    """ 
    
    def perform(self, data):
        if data == 1:
            self.next = self.lookup_menu
        if data == 9:
            self.app_event("EXIT")

if __name__ == "__main__":

    welcome_msg = """
======== Welcome to A.T.M.O.S.! ========
[Advance Testing & Mission Ops Software]
----------------------------------------"""
    
    mode_select = {
        1: "1. Test",
        2: "2. Simulation",
        3: "3. Mission Ops",
        9: "9. Exit",
    }

    mode_prompt = Prompt("Select one of the following options:", int, mode_select)
    welcome = WelcomeScreen(welcome_msg, mode_prompt)
    app = App([welcome,], welcome)

    app.run()