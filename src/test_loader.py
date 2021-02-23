from importlib import import_module
from os import listdir, path

class DynamicImporter:
    """
    Allows for dynamic loading of test classes into the TestLoader at runtime
    IMPORTANT: This is a singleton class!
    NOTE: This is probably not "pythonic" but it works, so...
    """

    # TODO: Add hot-reloading so that tests written while an ATMOS instance is running can be
    #       included automatically

    _instance = None
    class_list = {}  # a dictionary ("ClassName": Class,)

    def __init__(self):
        """
        Initializes the DynamicImporter instance.
        Traverses the files in the /testdata directory and imports classes with the naming
        convention: filename.py -> class FilenameTest
        """
        if DynamicImporter._instance is not None:
            raise Exception("DynamicImporter instance already exists!")
        DynamicImporter._instance = self

        test_path = path.join(path.dirname(path.abspath(__file__)), "testdata")
        files = listdir(test_path)

        for f in files:
            if f in ["test_module.py", "test_registry.py"]:
                continue
            name = "".join(f.split(".")[:-1])
            if name not in ["", "\n", "\r", "\r\n"] and f.endswith(".py"):
                module = import_module(f"testdata.{name}")  # import the module dynamically
                class_title = f"{name.title()}Test"
                try:
                    _class = getattr(module, class_title)  # get the class
                    self.class_list[class_title] = _class  # add the class to the class list
                except AttributeError:  # don't throw exceptions for files that don't have a test
                    continue
    
    @staticmethod
    def instance():
        """
        Static access method
        """
        if DynamicImporter._instance is None:
            DynamicImporter()
        return DynamicImporter._instance


class TestLoader:
    """
    Provides useful utilities to load test classes into the App
    """

    def __init__(self):
        self.menu = None
        self.importer = DynamicImporter.instance()
        self.library = self.importer.class_list
    
    def set_menu(self, menu):
        self.menu = menu

    def load(self, test_name: str):
        self.menu.load_test(self.library[test_name])
    
    def unload(self):
        self.menu.load_test(None)