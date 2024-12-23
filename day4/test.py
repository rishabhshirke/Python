import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    # def test_add_positive_numbers(self):
    #     self.assertEqual(add(1, 2), 4,"Error")

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()

# Possible test outcomes

    # OK – This means that all the tests are passed.
    # FAIL – This means that the test did not pass and an AssertionError exception is raised.
    # ERROR – This means that the test raises an exception other than AssertionError.


    # assertEqual() – This statement is used to check if the result obtained is equal to the expected result.
    # assertTrue() / assertFalse() – This statement is used to verify if a given statement is true or false.
    # assertRaises() – This statement is used to raise a specific exception.