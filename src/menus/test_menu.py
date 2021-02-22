# test_menu.py
# Contains the TestMenu class which displays the Test mode screen

from .config import MENU_TYPE
from .ui import Prompt

### Instance variables for TestMenu ###

# Test menu prompt
test_select = {
    1: "Load Test",
    2: "Check Connection",
    3: "Start Test",
    4: "Export Results",
    9: "Exit",
    0: "Home",
}

#######################################

class TestMenu(MENU_TYPE):
    """
    The test main menu
    """

    def __init__(self, loader, *args, **kwargs):
        """
        :precond: test_select must exist in the scope immediately outside of this method call
        :type test_select: dict
        :param loader: The TestLoader instance that will be used to load tests into this menu
        :type loader: TestLoader
        """
        super().__init__(*args, **kwargs)
        self.message = "======== TEST ========"
        self.prompt = Prompt(
            "Select an action:",
            int, test_select
        )
        self.loader = loader
        self.loader.set_menu(self)
        self.test = None
        self.test_kwargs = None
    
    def load_test(self, test):
        """
        Loads a given test instance

        :param test: The test (child of Test) to be loaded (or None if unloading)
        :type test: Test or None
        """
        self.test = test() if test is not None else test

    def perform(self, data):
        """
        Test menu options are Load Test, Check Connection, Start Test, Export Results, Exit, Home.
        """

        if data == 1:
            # Load test
            # self.next = self.lookup_menu("TestLoaderMenu")
            # self.test = sample.SampleTest()  # TODO ^^ implement this instead
            self.loader.unload()
            self.loader.load("SampleTest")  # 0 is a placeholder for now until better loading is implemented
            self.message += f"\nLoaded: {self.test.__class__.__name__}"  # This will keep adding
                                                                         # but never removing...

        elif data == 2:
            # Check connection
            if self.test._check_connection():
                print("Connection is good!")
            else:
                print("Connection not found!")

        elif data == 3:
            # Start test
            self.test._run_full()

        elif data == 4:
            # Export results
            # self.next = self.lookup_menu("TestExportMenu")
            self.test._export(f"testdata/{self.test.__class__.__name__}_results.json")  # TODO ^^

        elif data == 9:
            self.app_event("EXIT")

        elif data == 0:
            self.next = self.lookup_menu("WelcomeScreen")