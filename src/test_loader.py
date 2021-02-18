from testdata.test_registry import *

class TestLoader:
    """
    Provides useful utilities to load test classes into the App
    """

    def __init__(self):
        self.menu = None
        self.library = [
            SampleTest,
        ]
    
    def set_menu(self, menu):
        self.menu = menu

    def load(self, test):
        self.menu.load_test(SampleTest())  # TODO make this actually load different tests...
    
    def unload(self):
        self.menu.load_test(None)