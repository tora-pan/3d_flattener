import unittest
from flatten3d import flatten_array
import io
import sys

class TestFlatten(unittest.TestCase):

    def test_flatten_array(self):
        '''
        Method to test flattening of the passed in 3d array and catch 2 edge cases
        '''
        returned_result = flatten_array([[1,2,3], [4,5,6], [7,8,9]])
        expected_result = [1,4,7,2,5,8,3,6,9]

        # confirm that the 3d array gets flattened correctly
        self.assertEqual(returned_result, expected_result)

        # testing console logs are printed correctly
        first_output = io.StringIO()
        sys.stdout = first_output #redirect stdout
        
        # confirm inner arrays must be the same length warning is displayed
        flatten_array([[1,2], [1,2], [1]])
        sys.stdout = sys.__stdout__ # reset redirect
        self.assertEqual(first_output.getvalue(), "Please make sure that the inner arrays are the same lengths.\n")
        
        # confirm not 3 dimensional array warning is displayed
        second_output = io.StringIO()
        sys.stdout = second_output #redirect stdout
        flatten_array([[1,23], [1,23]])    
        sys.stdout = sys.__stdout__ # reset redirect
        self.assertEqual(second_output.getvalue(), "Please pass in a 3 dimensional array with equal lengths.\n")


if __name__ == '__main__':
    unittest.main()