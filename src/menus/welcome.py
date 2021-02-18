# welcome.py
# Contains the WelcomeScreen class which displays the opening menu for ATMOS (mode select)

from .config import MENU_TYPE
from .ui import Prompt

### Instance variables for the WelcomeScreen menu ###

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

#####################################################

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