from sweaterno8_test import sweaterNo8Test
import unittest
# Todo: aggregate all tests into this file

def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(sweaterNo8Test('test_validSizes'))
    suite.addTest(sweaterNo8Test('test_invalidSizes'))
    suite.addTest(sweaterNo8Test('test_validGauge'))
    suite.addTest(sweaterNo8Test('test_validSizes'))
    suite.addTest(sweaterNo8Test('test_invalidGauge'))
    return suite

if __name__ == '__main__':
    #Todo: set up logic to delete existing test log files
    runner = unittest.TextTestRunner()
    result = runner.run(create_test_suite())
    if len(result.errors) == 0 and len(result.failures) == 0:
        print("All Test Ran Successfully")