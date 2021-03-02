# test_loader_menu.py
# Contains the TestLoaderMenu class which prompts the user to select a test to load into ATMOS

from os import listdir, path
from typing import Any

from .config import MENU_TYPE
from .ui import Prompt

# ## Instance variables for TestLoaderMenu ## #


class TestLoaderMenu(MENU_TYPE):
    """
    The test loader menu (prompts user to select a test)
    """

    def __init__(self, loader, *args, **kwargs):
        """
        :precond: test_loader_select must exist in a local or non-local scope
        :type test_loader_select: dict
        :param loader: The TestLoader instance that will be used to load the selected test
        :type loader: TestLoader
        """
        super().__init__(*args, **kwargs)
        self.message = "======== LOAD ========"
        self.loader = loader
        self.prompt_options = {}

        test_path = path.join(path.dirname(path.abspath(__file__)), "..", "testdata")
        files = listdir(test_path)

        for f in files:
            if f in [
                "test_module.py",
                "test_registry.py",
                "connections.py",
            ]:  # blacklist of py files
                continue
            name = "".join(f.split(".")[:-1])
            if name not in ["", "\n", "\r", "\r\n"] and f.endswith(".py"):
                self.prompt_options[
                    len(self.prompt_options.keys()) + 1
                ] = f"{name.title()}Test"
        self.prompt = Prompt(
            "Select one of the following tests:", Any, self.prompt_options
        )
        self.selection = None

    def perform(self, data):
        """
        Test Loader menu options are a list of strings corresponding to test names
        """
        self.loader.unload()
        if isinstance(data, str):
            self.loader.load(str(data))
        elif isinstance(data, int):
            self.loader.load(self.prompt_options[data])
        else:
            pass  # But we should probably handle this better

        self.next = self.lookup_menu("TestMenu")
