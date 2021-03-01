# test_loader_menu.py
# Contains the TestLoaderMenu class which prompts the user to select a test to load into ATMOS

from os import listdir, path

from .config import MENU_TYPE, nav_select
from .ui import Prompt

### Instance variables for TestLoaderMenu ###

# Test loader menu prompt
test_loader_select = {
    # TODO: Create a method to populate this
    #       Maybe make it an instance variable of TestLoaderMenu
}

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

        test_path = path.join(path.dirname(path.abspath(__file__)), "..", "testdata")
        files = listdir(test_path)

        prompt_options = {}

        for f in files:
            if f in ["test_module.py", "test_registry.py", "connections.py"]:  # blacklist of py files
                continue
            name = "".join(f.split(".")[:-1])
            if name not in ["", "\n", "\r", "\r\n"] and f.endswith(".py"):
                prompt_options[len(prompt_options.keys())+1] = f"{name.title()}Test"
        self.prompt = Prompt(
            "Select one of the following tests:",
            str, prompt_options
        )
        self.selection = None

    def perform(self, data):
        """
        Test Loader menu options are a list of strings corresponding to test names
        """
        self.loader.unload()
        self.loader.load(str(data))
        # TODO Remove me, I'm just here for the debugging
        print(f"Loaded {data}!")  # TODO: ALlow users to enter a digit corresponding to the test they want
        
        self.next = self.lookup_menu("TestMenu")