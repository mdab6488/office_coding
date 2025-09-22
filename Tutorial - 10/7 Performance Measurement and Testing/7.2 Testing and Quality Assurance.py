# Python includes robust testing frameworks in its standard library, which is crucial for maintaining code quality in web applications.

"""7.2.1 doctest for Example-Based Testing"""
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    
    >>> print(average([20, 30, 70]))
    40.0
    >>> print(average([1, 2, 3, 4]))
    2.5
    """
    return sum(values) / len(values)

# Run doctests
import doctest
doctest.testmod()

"""7.2.2 unittest for Comprehensive Testing"""
import unittest

# Example function to test
def format_name(first, last):
    return f"{first.title()} {last.title()}"

# Test class
class TestFormatName(unittest.TestCase):
    
    def test_normal_names(self):
        self.assertEqual(format_name('john', 'doe'), 'John Doe')
        
    def test_empty_names(self):
        with self.assertRaises(AttributeError):
            format_name('', '')
            
    def test_mixed_case(self):
        self.assertEqual(format_name('aLaN', 'tUrInG'), 'Alan Turing')

# Run tests
if __name__ == '__main__':
    unittest.main()
    
# These testing tools are essential for ensuring the reliability and stability of web applications, particularly as they grow in complexity 