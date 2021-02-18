from .test_module import Test

class SampleTest(Test):
    def execute(self):
        print("Hello, world!")
        return True
