# sim_menu.py
# Contains the class SimMenu which displays the Simulation mode screen

from .config import MENU_TYPE, nav_select
from .ui import Prompt

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