#!/usr/local/bin/python3.8

# atmos.py
# Contains the entrypoint for the ATMOS software
from menus.menu import App, TerminalMenu
from menus.ui import Prompt, TUI
from menus import (
    mops_menu,
    sim_menu,
    test_menu,
    welcome,
)
from test_loader import TestLoader
from testdata import sample

# Application Entrypoint
if __name__ == "__main__":

    tl = TestLoader()
    
    welc = welcome.WelcomeScreen()      # Main menu (mode select)
    test = test_menu.TestMenu(tl)         # Test menu
    sim = sim_menu.SimMenu()            # Simulation menu
    mos = mops_menu.MissionOpsMenu()    # Mission Ops menu

    app = App.instance()
    app.run(welc)
