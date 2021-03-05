# config.py
# Contains settings and system-wide variables for the menus system

from .menu import TerminalMenu

# Change this to a different class if moving away from a TUI
MENU_TYPE = TerminalMenu

# Basic navigation menu prompt
nav_select = {
    1: "Back",
    9: "Exit",
    0: "Home",
}
