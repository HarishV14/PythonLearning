import unittest
import roman1,roman2

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
.'''

class KnownValues(unittest.TestCase):
    '''this to run the value for the test kept as the input'''
    known_values = (
        (1, 'I'),
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
        # (1000, 'M'),
        (31, 'XXXI'),
        (148, 'CXLVIII'),
        (294, 'CCXCIV'),
        (312, 'CCCXII'),
        (421, 'CDXXI'),
        (528, 'DXXVIII'),
        (621, 'DCXXI'),
        (782, 'DCCLXXXII'),
    )

    '''In this we have convert the integer given in the input using the function to_roman
    writen in the roman1.py file we check that output given know value correct using
    assertEqual'''
    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman1.to_roman(integer)
            self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        '''from_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman2.from_roman(numeral)
            self.assertEqual(integer, result)

'''It is to check deeply of the inputs more testing the value we give the condition and 
raise the error in the to_roman function if it fail raise error using assertRaises in the 
unit testing '''

class RoundtripCheck(unittest.TestCase):
    def test_roundtrip(self):
        '''from_roman(to_roman(n)) == n for all n'''
        for integer in range(1, 782):
            numeral = roman1.to_roman(integer)
            result = roman2.from_roman(numeral)
            self.assertEqual(integer, result)
        
class FromRomanBadInput(unittest.TestCase):
    
    def test_too_many_repeated_numerals(self):
        '''from_roman should fail with too many repeated numerals'''
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, s)

    def test_repeated_pairs(self):
        '''from_roman should fail with repeated pairs of numerals'''
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, s)

    def test_malformed_antecedents(self):
        '''from_roman should fail with malformed antecedents'''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, s)


class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input 
        should be failed condition to check it is working properly should not provide current input in 
        third field '''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 783)  # Test with a value greater than 783

    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 0)

    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, -1)
    
    def test_nonInteger(self):
        '''to_roman should fail with non Integer inputs'''
        self.assertRaises(roman1.nonIntergerError,roman1.to_roman,2.34)


''' unittest.main(): 
        This runs all the test cases defined in the script when the script is executed directly.
        It discovers and executes test methods in the KnownValues class'''

if __name__ == '__main__':
    unittest.main()
