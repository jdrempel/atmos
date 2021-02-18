from .test_module import Test

class SampleTest(Test):
    """
    This is a sample test that is used for general debugging of ATMOS
    """

    def execute(self):
        """
        The execute() method should always be overridden to contain whatever test procedures
        are supposed to be run by ATMOS for this test. It should return True if there are no
        exceptions, False otherwise.
        """
        print("Hello, world!")
        return True
