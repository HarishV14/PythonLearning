import roman
import unittest
'''Know values were given
 KnownValues: This class inherits from unittest.TestCase, 
               which provides various methods for writing and running tests.
 
 known_values: This tuple contains pairs of integers and their expected Roman numeral representations. 
               These are used as test cases to validate the toRoman() function.

 test_to_roman_known_values: This method tests the toRoman() function.
            for integer, numeral in self.known_values: 
                         Iterates over each integer and its corresponding Roman numeral.
            result = roman.toRoman(integer): 
                         Calls the toRoman() function from the roman module with the integer value.
            self.assertEqual(numeral, result): 
                          Compares the result from toRoman() with the expected Roman numeral. 
                          If they do not match, the test will fail.
 unittest.main(): 
        This runs all the test cases defined in the script when the script is executed directly.
        It discovers and executes test methods in the KnownValues class.'''
class KnownValues(unittest.TestCase):               
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'))        

    def test_to_roman_known_values(self):           
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman.toRoman(integer)   
            # print(result)    
            self.assertEqual(numeral, result)       

if __name__ == '__main__':
    unittest.main()